/*
	____________________________________________________________________
	####################################################################
						UNIWALLET FRONTEND API
	####################################################################
	____________________________________________________________________

	JQuery is required
*/

function Auth(){
	Token = function(){
		this.set = function(token){
			localStorage.setItem("uniwallettoken", token)
		}
		this.get = function(){
			return localStorage.getItem("uniwallettoken")
		}
		this.destroy = function(){
			localStorage.removeItem("uniwallettoken")
		}
		this.exists = function(){
			if (Auth.Token.get())
				return true
			else
				return false
		}
	}
	this.signIn = function(token){
		this.Token.set(token)
	}
	this.signOut =function(){
		this.Token.destroy()
	}
	this.Token = new Token()
}


function Request(domain = "http://localhost:8000", module_name = "api"){
	this.send = function(data, route, method, callback){
		$.ajax({
			type: method,
			url: domain + "/" + module_name  + "/" + route,
			data: (method == "POST") ? JSON.stringify(data) : data,
			success: callback,
			cache: false,
			beforeSend: function(xhr) {
				if (Auth.Token.exists()){
					xhr.setRequestHeader('Authorization', 'Basic ' + Auth.Token.get())
				}
			},
			dataType: 'json'
		})
	}
}



function Page(){
	this.get_input = function(class_name){
		var inputs = document.getElementsByClassName(class_name)
		var input_dict = {}
		for (var i = 0; i < inputs.length; i++) {
			if (inputs[i].name) {
				input_dict[inputs[i].name] = inputs[i].value
			}
		}
		return input_dict
	}
	this.redirect = function(address){
		$(location).attr('href', address)
	}
	this.fill = function(id, content){
		document.getElementById(id).innerHTML = content
	}
	this.listen = function(id, callback, event_type = "click"){
		document.getElementById(id).addEventListener(event_type, callback)
	}
	this.popup = function(header, body, header){
		window.alert("hello")
	}
}

function HTML_Factory(){

	Data_Table = function(table_id, columns, resource_name, data, method = "GET"){
		table_columns = []
		for (var i = 0; i < columns.length; i++) {
			table_columns[i] = { "data": columns[i] }
		}
		console.log(table_columns)
		this.make = function(func_new, func_edit, func_delete){
			var table = $(table_id).DataTable( {
				lengthChange: false,
				ajax: {
					url: "/api/" + resource_name + "/fetch",
					data: data,
					dataFilter: function(data){
						var json = jQuery.parseJSON( data );
						json.recordsTotal = json.content.length;
						json.recordsFiltered = json.content.length;
						json.data = json.content;
						return JSON.stringify( json ); // return JSON string
					},
					cache: false,
					beforeSend: function(xhr) {
						if (Auth.Token.exists()){
							xhr.setRequestHeader('Authorization', 'Basic ' + Auth.Token.get())
						}
					},
					method: method
				},
				language: {
					url: "//cdn.datatables.net/plug-ins/1.10.15/i18n/Portuguese-Brasil.json",
				},
				columns: table_columns,
				initComplete: function(){
					//showButtons();
				},
				dom: 'Bfrtip',
				buttons: [
					{
						text: 'Novo',
						action: func_new
					},
					{
						extend: 'selectedSingle',
						text: 'Editar',
						action: func_edit
					},
					{
						extend: 'selected',
						text: 'Remover',
						action: func_delete
					}
				],
				select: true
			} );
		}
	}


	this.make_table = function(fields, data, title){
		ths = ''
		for (var i = 0; i < fields.length; i++) ths += this.make_tag('th', fields[i])
		tr = this.make_tag('tr', ths)
		thead = this.make_tag('thead', tr)
		trs = ''
		for (var i = 0; i < data.length; i++) {
			tds = ''
			for (var j = 0; j < fields.length; j++) tds += this.make_tag('td', data[i][fields[j]])
			trs += this.make_tag('tr', tds)
		}

		if (trs.length){
			tbody = this.make_tag('tbody', trs)
		} else {
			tbody = ''
		}

		return this.get_snippet()['table'].replace('{{thead}}', thead).replace('{{tbody}}', tbody).replace('{{title}}', title)
	}

	this.make_form = function(fields, data){
		form_fields = ""
		for (var i = 0; i < fields.length; i++) {
			if (data[fields[i]])
				value = data[fields[i]]
			else
				value = ""
			form_fields += this.get_snippet()['form-field'].replace('{{label}}', fields[i]).replace('{{type}}', 'text').replace('{{name}}', fields[i]).replace('{{value}}', value)
		}
		var form = this.get_snippet()['form'].replace('{{fields}}', form_fields)
		return form
	}

	this.get_snippet = function(id = "tablecrud"){
		return {
			'table':'<div class="table-responsive">' +
						'<h2>{{title}}</h2>' +       
						'<table id="' + id + '" class="table table-striped table-bordered" width="100%" cellspacing="0">' +
						'{{thead}}' +
						'{{tbody}}' +
						'</table>' +
					'</div>',
			'form-field': '<div class="form-group">' +
								'<label>{{label}}</label>' +
								'<input type="{{type}}" class="form-control" name={{name}} value={{value}}>' +
							'</div>',
			'form': '<table>' +
						'{{fields}}' +
						'<div class="btn-group">' +
							'<a href="#" class="btn btn-primary">Salvar</a>' +
							'<a href="#" class="btn btn-default">Cancelar</a>' +
						'</div>' +
					'</table>'
		}
	}



	this.make_tag = function(tag_name, content){
		return ('<' + tag_name + '>' + content + '</' + tag_name + '>')
	}

	this.make_datatable = function(columns, resource_name, data, method){

		console.log(columns, resource_name, data, method)
		create = function(e, dt, button, config){
			Page.fill('mainform', HTML_Factory.make_form(columns, {}))
		}
		edit = function(e, dt, button, config){
			//alert("modal de edição aqui")
			var data = dt.rows({ selected: true }).data()
			console.log(data[0])
			Page.fill('mainform', HTML_Factory.make_form(columns, data[0]))
		}
		del = function(e, dt, button, config){

			if(confirm("Deseja mesmo remover a seleção?")){
				data = dt.rows({ selected: true }).data()
				ids_list = []
				for (var i = 0; i < data.length; i++) {
					ids_list[i] = {id: data[i].id}
				}
				Request.send({data: ids_list}, resource_name + '/delete', 'POST', function(response){
					window.alert(response.content)
					dt.rows({ selected: true }).remove().draw()
				})
			}
		}
		datatable = new Data_Table('#tablecrud', columns, resource_name, data, method).make(create, edit, del)
	}
}


var Page = new Page()
var Request = new Request()
var Auth = new Auth()
var HTML_Factory = new HTML_Factory()