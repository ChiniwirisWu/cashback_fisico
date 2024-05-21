window.onload = async (e)=>{
	let source = "https://api.qrserver.com/v1/create-qr-code/?data=gonzalo&size=500x500&color=900&bgcolor=090"
	createQR(source)
	readQR(source)
}

async function readQR(source){
	let img_ref = encodeURIComponent(source)
	let query = await fetch(`https://api.qrserver.com/v1/read-qr-code/?fileurl=${img_ref}`).then(response=>response.json())
	console.log(query)
}

async function createQR(source){
	const img = document.getElementById('qr-img')
	let query = await fetch(source)
	let img_url = query.url
	img.src = img_url 
}
