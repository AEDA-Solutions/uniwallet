var data = "A";
console.log("0x" + data.charCodeAt(0).toString(16));


data = "1"
result = ""

for (var i = 0; i < data.length; i++) {
	result += "0x" + data[i].charCodeAt(0).toString(16)

}

console.log(result)