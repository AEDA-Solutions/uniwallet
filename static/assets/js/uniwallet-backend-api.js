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
			return localStorage.uniwallettoken
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
	this.Token = new Token()
}


function Request(domain = "http://localhost:8000", module_name = "api"){
	this.send = function(data, route, method, callback){
		$.ajax({
			type: method,
			url: domain + "/" + module_name  + "/" + route,
			data: (method == "POST") ? JSON.stringify(data) : data,
			success: callback,
			dataType: 'json'
		});
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

var Page = new Page()
var Request = new Request()
var Auth = new Auth()