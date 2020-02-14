#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#
#  Copyright 2017 Daniel Cruz <bwb0de@bwb0dePC>
#  CLI Base configfile
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

import os
import asyncio
import time

from tempfile import gettempdir
from string import punctuation
from collections import OrderedDict
from subprocess import getoutput

from .cli_tools import verde, vermelho, amarelo, select_op, return_obj_from_dict
from .cli_tools import load_json, save_json, point_to_json, append_index_do_dict

def timestamp(mode=None):
    if mode == "mkid":
        from subprocess import getoutput
        return time.strftime("{}%Y%m%d%H%M%S".format(username[0:3].upper()), time.localtime())
    
    elif mode == "long":
        mes_corrente = time.strftime("%m", time.localtime())

        mes = {}
        mes['01'] = 'janeiro'
        mes['02'] = 'fevereiro'
        mes['03'] = 'março'
        mes['04'] = 'abril'
        mes['05'] = 'maio'
        mes['06'] = 'junho'
        mes['07'] = 'julho'
        mes['08'] = 'agosto'
        mes['09'] = 'setembro'
        mes['10'] = 'outubro'
        mes['11'] = 'novembro'
        mes['12'] = 'dezembro'

        nome_mes = mes[mes_corrente]
        
        return time.strftime("%d de "+nome_mes+" de %Y", time.localtime())
    else:
        return time.strftime("%Y-%m-%d %H:%M:%S %a", time.localtime())


def get_col_width(field_name, list_of_dicts):
    width = 0
    for dict_item in list_of_dicts:
        if dict_item.get(field_name):
            if len(dict_item[field_name]) > width:
                width = len(dict_item[field_name])
    return (field_name, width+2)


def get_dict(field_name, field_value,  list_of_dicts):
    for dict_item in list_of_dicts:
        if dict_item[field_name] == field_value:
            yield dict_item


def get_all_values_form_field(field_name, list_of_dicts):
    #r = []
    for dict_item in list_of_dicts:
        yield dict_item[field_name]#r.append(dict_item[field_name])
    #return r


def get_all_users_tags(users_list_of_dicts):
    marcadores = []
    for usuario in users_list_of_dicts:
        if usuario.get("marcador"):
            for marcador in usuario['marcador']:
                if marcador not in marcadores:
                    marcadores.append(marcador)
    marcadores.sort()
    return marcadores


def get_all_users_tags_idx(users_list_of_dicts):
    marcadores_idx = {}
    for usuario in users_list_of_dicts:
        if usuario.get("marcador"):
            for marcador in usuario['marcador']:
                marcadores_idx = append_index_do_dict(marcador, users_list_of_dicts.index(usuario), marcadores_idx)
    return marcadores_idx


def calculate_col_width(test=False):
    loop2 = asyncio.get_event_loop()
    col_width = loop2.run_until_complete(asyncio.gather(
        get_col_width_nfo('identificador', users_list_of_dicts),
        get_col_width_nfo('nome', users_list_of_dicts),
        get_col_width_nfo('eml', users_list_of_dicts),
        get_col_width_nfo('uid', dados_profissionais),
        get_col_width_nfo('prof_nome', dados_profissionais),
        get_col_width_nfo('prof_eml', dados_profissionais),
        get_col_width_nfo('numero_sei', dados_processos),
        get_col_width_nfo('assunto', dados_processos),
        get_col_width_nfo('motivo', dados_processos),
        get_col_width_nfo('cotista', dados_estudos),
        get_col_width_nfo('turno_curso', dados_processos),
        get_col_width_nfo('motivos_estudo', dados_processos),
        get_col_width_nfo('campus', dados_processos),
        get_col_width_nfo('atd_t', dados_atendimentos),
    ))

    col_wid = {}
    col_wid['identificador'] = col_width[0]
    col_wid['nome_usuario'] = col_width[1]
    col_wid['eml_usuario'] = col_width[2]
    col_wid['uid'] = col_width[3]
    col_wid['nome_profissional'] = col_width[4]
    col_wid['eml_profissional'] = col_width[5]
    col_wid['numero_sei'] = col_width[6]
    col_wid['assunto'] = col_width[7]
    col_wid['motivo'] = col_width[8]
    col_wid['timestamp'] = ('timestamp', len(timestamp()) + 2)
    col_wid['cotista'] = col_width[9]
    col_wid['turno_curso'] = col_width[10]
    col_wid['motivos_estudo'] = col_width[11]
    col_wid['campus'] = col_width[12]
    col_wid['atd_t'] = col_width[13]

    save_json(col_wid, arquivo_col_wid)

    return col_wid


def get_info_from_index(identificador, set_de_dados, index_de_dados):
    for s in index_de_dados:
        if s['set_de_dados'] == set_de_dados:
            return s['dados'].get(identificador)


def show_nfo_frag(identificador, set_de_dados, arquivo_de_dados, index_de_dados, print_info=True):
    ret_nfo = get_info_from_index(identificador, set_de_dados, index_de_dados)
    if ret_nfo:
        for i in ret_nfo:
            if print_info:
                nfo = arquivo_de_dados[i]
                if nfo.get('timestamp'):
                    print('Data e hora:', nfo['timestamp'])
                if nfo.get('numero_sei'):
                    print('Número no SEI:', vermelho(nfo['numero_sei']))
                if nfo.get('assunto'):
                    print('Assunto do processo:', nfo['assunto'])
                if nfo.get('motivo'):
                    print('Motivo:', nfo['motivo'])                                        
                if nfo.get('nome'):
                    print('Nome:', amarelo(nfo['nome']), '('+nfo['eml']+')')
                if nfo.get('sexo'):
                    print('Sexo:', nfo['sexo'])
                if nfo.get('curso'):
                    print('Curso:', nfo['curso'])
                if nfo.get('atd_t'):
                    print(' » '+nfo['atd_t'])
                print('')




def show_nfo_frag_by_nome(identificador, arquivo_de_dados, index_de_dados):
    identificador_init = identificador[0]
    set_de_nomes = {}
    for sets in index_de_dados:
        if sets['set_de_dados'] == 'nome':
            set_de_nomes = sets['dados']
    try:
        entries = set_de_nomes.get(identificador_init).get(identificador)
        num_entries = len(entries)
    except:
        entries = []
        num_entries = 0
    
    if num_entries > 1:
        nomes_op = []
        for idx in entries:
            nomes_op.append(arquivo_de_dados[idx]['nome'])
        print(verde("Mais de um estudante possui registro do nome solicitado em seu nome completo, selecione o estudante correto:"))
        op = select_op(nomes_op, 1)[0]
        op_idx = entries[nomes_op.index(op)]
        return arquivo_de_dados[op_idx]['identificador']
    
    elif num_entries == 0:
        print(vermelho("Registro não encontrado..."))
    
    else:
        return arquivo_de_dados[entries[0]]['identificador']



def save_target_info(identificador, list_of_dicts):
    for dict_item in list_of_dicts:
        if dict_item['identificador'] == identificador:
            save_json(dict_item, arquivo_usuario_alvo)



def numero_sei_mascara(num):
    m_num = num
    for char in punctuation:
        m_num = m_num.replace(char,'')
    return str(m_num[0:5]+'.'+m_num[5:11]+'/'+m_num[11:15]+'-'+m_num[15:])


def numero_identificador_mascara(num):
    #Define user ID format here
    m_num = num
    for char in punctuation:
        m_num = m_num.replace(char,'')
    return str(m_num[0:2]+'/'+m_num[2:])



async def point_to_json_file(arquivo):
    return load_json(arquivo)



async def get_col_width_nfo(field_name, data_set):
    return get_col_width(field_name, data_set)



async def get_col_label(formulario):
    id_and_label = {}
    for i in formulario['form_questions']:
        id_and_label[i['id']] = i['enunciado']
    return id_and_label


#Machine and system user info
hostname = getoutput("hostname")
username = getoutput("whoami")


#Read info from /etc/cli/cli_tools.conf
home_folder = getoutput("echo $HOME")
tmp_folder = gettempdir()
app_root_folder = getoutput("cli-config read PASTA_RAIZ_DO_PROGRAMA")
db_folder = getoutput("cli-config read PASTA_DE_DADOS")
security_folder = getoutput("cli-config read PASTA_DE_SEGURANCA")
working_folder = getoutput("cli-config read PASTA_DE_TRABALHO")
device = getoutput("cli-config read DEVICE_TYPE")
send_email_automaticaly = bool(getoutput("cli-config read ENVIO_AUTOMATICO_EMAIL"))
work_with_fragments = bool(getoutput("cli-config read ENVIO_DE_FRAGMENTOS"))

rclone_drive=getoutput("cli-config read RCLONE")

if device == "Termux":
    tmp_folder = getoutput("echo $TMPDIR")


#Setting global paths to cli base folders and files
fragments_folder = os.sep.join([db_folder, "fragmentos"])
index_folder = os.sep.join([db_folder, "indexados"])
forms_folder = os.sep.join([app_root_folder, "cli/formularios"])

emitted_fragments_file = os.sep.join([fragments_folder, "emitidos.json"])
received_fragments_file = os.sep.join([fragments_folder, "recebidos.json"])
arquivo_atendimentos = os.sep.join([db_folder, "atendimentos.json"])
arquivo_usuarios = os.sep.join([db_folder, "usuarios.json"])
arquivo_profissionais = os.sep.join([db_folder, "profissionais.json"])
arquivo_processos = os.sep.join([db_folder, "processos.json"])
arquivo_corrigidos = os.sep.join([db_folder, "corrigidos.json"])
arquivo_index = os.sep.join([index_folder, "index_db.json"])
arquivo_col_wid = os.sep.join([index_folder, "col_wid.json"])
arquivo_sex_info = os.sep.join([index_folder, "sex_info.json"])
arquivo_estudos = os.sep.join([db_folder, "estudos.json"])
arquivo_usuario_alvo = os.sep.join([home_folder, '.current_target'])
arquivo_modelo_ppaes = os.sep.join([app_root_folder, "cli/modelos/ppaes.odt"])
arquivo_modelo_ppaes_detalhado = os.sep.join([app_root_folder, "cli/modelos/ppaes_det.odt"])
arquivo_modelo_ccc = os.sep.join([app_root_folder, "cli/modelos/criacao-cc.odt"])

lista_pase = os.sep.join([db_folder, "lista_pase.json"])
lista_moradia = os.sep.join([db_folder, "lista_moradia.json"])
lista_creche = os.sep.join([db_folder, "lista_creche.json"])
lista_transporte = os.sep.join([db_folder, "lista_transporte.json"])

formulario_atendimentos = os.sep.join([forms_folder, "form_atendimento.json"])
formulario_novo_usuario = os.sep.join([forms_folder, "form_novo_usuario.json"])
formulario_novo_processo = os.sep.join([forms_folder, "form_processos.json"])
formulario_registro_de_correcao = os.sep.join([forms_folder, "form_corrigidos.json"])
formulario_estudo_estudante = os.sep.join([forms_folder, "form_estudo_socioeconomico.json"])

#Carregando arquivos de dados
loop = asyncio.get_event_loop()
dados = loop.run_until_complete(asyncio.gather(
    point_to_json_file(arquivo_atendimentos),
    point_to_json_file(arquivo_usuarios),
    point_to_json_file(arquivo_profissionais),
    point_to_json_file(arquivo_processos),
    point_to_json_file(arquivo_corrigidos),
    point_to_json_file(arquivo_index),
    point_to_json_file(arquivo_estudos),
    point_to_json_file(lista_pase),
    point_to_json_file(lista_moradia),
    point_to_json_file(lista_transporte),
    point_to_json_file(lista_creche)                
))

dados_atendimentos = dados[0]
users_list_of_dicts = dados[1]
dados_profissionais = dados[2]
dados_processos = dados[3]
dados_processos_pend = tuple(get_dict('resultado', '', dados_processos))
dados_corrigidos = dados[4]
dados_index = dados[5]
dados_estudos = dados[6]
dados_lista_pase = dados[7]
dados_lista_moradia = dados[8]
dados_lista_transporte = dados[9]
dados_lista_creche = dados[10]

col_wid_test = int(getoutput("if [ -f {} ]; then echo 1; else echo 0; fi".format(arquivo_col_wid)))

if col_wid_test == 1:
    col_wid = load_json(arquivo_col_wid)
    #
else:
    col_wid = calculate_col_width()
    #calculate_col_width()

#Custom configurations - SPS
matriculas = get_all_values_form_field('identificador', users_list_of_dicts)

periodo_corrente = "2º/2019"
formato_lista_fragmentos = "emitidos-{}@{}.json".format(username, hostname)

etiquetas = {}
etiquetas['identificador'] = "Identificador"
etiquetas['nome_usuario'] = "Nome"
etiquetas['eml_usuario'] = "e-Mail"
etiquetas['uid'] = "ID de Login"
etiquetas['nome_profissional'] = "Nome do Profissional"
etiquetas['eml_profissional'] = "e-Mail"
etiquetas['numero_sei'] = "Número do processo"
etiquetas['assunto'] = "Assunto"
etiquetas['motivo'] = "Motivo"
etiquetas['timestamp'] = "Data e hora"



