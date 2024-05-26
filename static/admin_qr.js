import QrScanner from './node_modules/qr-scanner/qr-scanner.min.js'

let $message = document.getElementById('scanner-message')
let $video = document.getElementById('scanner-frame')
let $overlay = document.getElementById('scanner-overlay')
let $add_btn = document.getElementById('add-btn')
let $remove_btn = document.getElementById('remove-btn')
let $form = document.getElementById('cashback-form')
let $user_hash_inp = document.getElementById('user_hash')

console.log($remove_btn)
$overlay.style.border = '5px dotted #fff'

const scanner = new QrScanner(
	$video,
	result => {
		$message.textContent = `User ${result.data} detected.`
		$user_hash_inp.value = result.data
		console.log(result)
	},
	Option = {
		'prefereceCamera': 'environment',
		'maxScansPerSecond': 10,
		'highlightScanRegion': true,
		'highlightCodeOutline':true,
		'overlay':$overlay
	}
)

$form.addEventListener('submit', (e)=>{
	e.preventDefault()
})

$add_btn.addEventListener('click', async (e)=>{
	let formData = new FormData($form)		
	let data = Object.fromEntries(formData.entries())
	let url = 'add_to_budget'
	let query = await fetch(url, {
		method: 'POST',
		body: JSON.stringify(data),
		headers: {'Content-Type':'application/json', 'X-CSRFToken': data.csrfmiddlewaretoken}
	})
	if(query.status == 200){
		$message.textContent = `${(data.amount * 0.09).toFixed(2)}$ se ha añadido a ${data.user_hash}`
	} else{
		$message.textContent = `No se ha realizado ninguna operación`
	}
})


$remove_btn.addEventListener('click', async (e)=>{
	console.log('click')
	let formData = new FormData($form)		
	let data = Object.fromEntries(formData.entries())
	let url = 'remove_from_budget'
	let query = await fetch(url, {
		method: 'POST',
		body: JSON.stringify(data),
		headers: {'Content-Type':'application/json', 'X-CSRFToken': data.csrfmiddlewaretoken}
	})
	if(query.status == 200){
		$message.textContent = `${data.amount}$ se ha removido a ${data.user_hash}`
	} else{
		$message.textContent = `No se ha realizado ninguna operación`
	}
})

scanner.start()

