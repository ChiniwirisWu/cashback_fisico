window.onload = async (e)=>{
	let source = "https://api.qrserver.com/v1/create-qr-code/?data=gonzalo&size=500x500&color=000&bgcolor=687"
	createQR(source)
}

async function createQR(source){
	const img = document.getElementById('qr_img')
	let query = await fetch(source)
	let img_url = query.url
	img.src = img_url 
}
