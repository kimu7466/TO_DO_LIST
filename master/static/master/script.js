document.addEventListener("DOMContentLoaded", ()=> {
    let list_li = document.querySelectorAll(".task_li")

    list_li.forEach(element => {
        let li_str = element.innerText;        
        if ( li_str.length >= 20 ){

            li_str = li_str.slice(0,20)
            li_str += "..."
            element.innerText = li_str
        }
    });

    // console.log(list_li);
})