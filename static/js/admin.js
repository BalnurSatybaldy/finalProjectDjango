function open_charity(charity_id) {
    var charities = document.getElementsByClassName("charity_info");
    for (var i = 0; i < charities.length; i++) {
        if (charities[i].id == "charity_"+charity_id) {
            charities[i].style.display = "block";
        } else {
            charities[i].style.display = "none";
            if (charity_id != 0) {
                document.getElementById("charity_text_"+charity_id).style.display = "block";
                document.getElementById("edit_form_"+charity_id).style.display = "none";
            }
        }
    }
}

//var charity_forms = document.getElementsByClassName("charity_form")
//console.log(charity_forms)
//for (var i = 0; i < charity_forms.length; i++) {
//    charity_forms[i].addEventListener("submit", function(event) {
//        alert("Hello piece of shit")
//        console.log(this);
//        event.preventDefault()
    //    alert("Hello you little shit")
    //    var type = this.getElementsByClassName("id_type")[0].value
    //    var needed_price = this.getElementsByClassName("id_needed_price")[0].value
    //
    //    if (type != "donation" && type != "volunteering") {
    //        alert("Type must be donation or volunteering")
    //        event.preventDefault()
    //    } else if (type == "donation" && needed_price == 0) {
    //        alert("Type is donation, so you have to enter the needed price")
    //        event.preventDefault()
    //    }
//    })
//}

$(".charity_form").submit(function(event) {
    console.log(this);
    var type = this.getElementsByClassName("id_type")[0].value
    var needed_price = this.getElementsByClassName("id_needed_price")[0].value

    if (type != "donation" && type != "volunteering") {
        alert("Type must be donation or volunteering")
        event.preventDefault()
    } else if (type == "donation" && needed_price == 0) {
        alert("Type is donation, so you have to enter the needed price")
        event.preventDefault()
    }
})

function edit_charity(id) {
    document.getElementById("charity_text_"+id).style.display = "none"
    document.getElementById("edit_form_"+id).style.display = "block"
}

function cancel_charity_editing(id) {
    document.getElementById("charity_text_"+id).style.display = "block"
    document.getElementById("edit_form_"+id).style.display = "none"
}