const copy_btns = document.querySelectorAll('.btnCopy');

let previous = null

copy_btns.forEach(btn=>{
    btn.addEventListener('click', e=>{
        e.preventDefault()
        const quote = e.target.dataset.quote
        navigator.clipboard.writeText(quote)
        e.target.textContent = 'Copied!'
        if(previous){
            previous.textContent = 'Copy'
        }
        previous = e.target


    })
})