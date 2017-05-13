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
}


function HTML_Factory(){
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
		tbody = this.make_tag('tbody', trs)

		return this.get_snippet()['table'].replace('{{thead}}', thead).replace('{{tbody}}', tbody).replace('{{title}}', title)
	}

	this.get_snippet = function(){
		return {
			'table':'<div class="table-responsive">' +
						'<h2>{{title}}</h2>' +       
						'<table class="table table-striped">' +
						'{{thead}}' +
						'{{tbody}}' +
						'</table>' +
					'</div>'
		}
	}

	this.make_tag = function(tag_name, content){
		return ('<' + tag_name + '>' + content + '</' + tag_name + '>')
	}
}



var Page = new Page()
var Request = new Request()
var Auth = new Auth()
var HTML_Factory = new HTML_Factory()