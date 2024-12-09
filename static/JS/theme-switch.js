let darkmode = localStorage.getItem('darkmode')


const themeSwitch = document.getElementById("theme-switch")
console.log('yeah i dont get this shit.. oh hi')
const enableDarkmode = () => {
    document.body.classList.add('darkmode')
    localStorage.setItem("darkmode", 'active')
}

const disableDarkmode = () => {
    document.body.classList.remove('darkmode')
    localStorage.setItem("darkmode", null)
}



themeSwitch.addEventListener("click", () => {
    if (darkmode != "active"){
        enableDarkmode()
    }
    else{
        disableDarkmode()
    }
})

