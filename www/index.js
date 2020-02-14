/*****

Template básico de aplicativo Node.JS com o módulo 'express'.
Autor: @bwb0de
email: danielc@unb.br

*****/

//Importando módulos do a serem usados
var express = require('express'); //http framework
var handlebars = require('express-handlebars').create({defaultLayout:'main'}); //Definindo os padrões dos templates (handlebars)
var body_parser = require('body-parser'); //para obter dados encaminhados via POST.
var fs = require("fs");


db_folder= "/home/danielc/Documentos/Devel/GitHub/sps_fup2/dados/";
//db_folder= "/outro/local/";

arquivo_usuarios = db_folder+"usuarios.json";
arquivo_atendimentos = db_folder+"atendimentos.json";
arquivo_processos = db_folder+"processos.json";

function read_json_file(target_json_file) {
	var rawdata = fs.readFileSync(target_json_file);
	var jsondata = JSON.parse(rawdata);
	return jsondata;
}


var app = express();

app.disable('x-powered-by'); //evitando que informações do servidor sejam exibidas
app.engine('handlebars', handlebars.engine);
app.set('view engine', 'handlebars');
app.use(body_parser.urlencoded({extended: true}));
app.set('port', process.env.PORT || 3000); //definindo a porta do servidor http
app.use(express.static(__dirname+"/public")); //definindo caminho de acesso ao conteúdo estático


app.get('/', function(req, res){
  res.render('index', {style_sheet: ['frontpage', 'w3']}); 
});


app.use(function(req, res, next){
  console.log('Looking for URL : ' + req.url); // Imprime tentativas de acesso a locais ou arquivos além da raiz do site e continua...
  next();
});

  
app.use(function(err, req, res, next){
  console.log('Error : ' + err.message); // Apanha o erro, apresenta-o no console e continua...
  next();
});


app.get('/listar_usuarios', function(req, res){
  nfo = read_json_file(arquivo_usuarios);
  res.render('listar_usuarios', {style_sheet: ['frontpage', 'w3'], nfo: nfo});
});


app.get('/listar_atendimentos', function(req, res){
  nfo = read_json_file(arquivo_atendimentos);
  res.render('listar_atendimentos', {style_sheet: ['frontpage', 'w3'], nfo: nfo});
});


app.get('/listar_processos', function(req, res){
  nfo = read_json_file(arquivo_processos);
  res.render('listar_processos', {style_sheet: ['frontpage', 'w3'], nfo: nfo});
});


app.get('/listar_processos_pendentes', function(req, res){
  nfo = read_json_file(arquivo_processos);
  res.render('listar_processos_pnd', {style_sheet: ['frontpage', 'w3'], nfo: nfo});
});


//Define página padrão de erro 404.
app.use(function(req, res) {
  res.type('text/html');
  res.status(404);
  res.render('404', { style_sheet: ['frontpage', 'w3'] });
});


//Define página padrão de erro 500.
app.use(function(err, req, res, next) {
  console.error(err.stack);
  res.status(500);
  res.render('500', { style_sheet: ['frontpage', 'w3'] });
});

var port = app.get('port');

app.listen(port, function(){
  console.log("Node iniciado em http://localhost:"+port+" aperte Ctrl-C para fechar.");
});
