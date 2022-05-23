let charity_id = 0;
let donation_form = document.getElementById("donate-form");
let volunteer_form = document.getElementById("volunteer-form");

function selectCharity(id, type) {
	charity_id = id;
	if (type == "donation") {
		var price = donation_form.getElementsByTagName("b")[0];
		price.innerText = document.getElementById(id+"_price").innerText;
	}
}

function submit_request(url, formData, type) {
	$.ajax({
	    type: "POST",
	    url: `${url}/${charity_id}/`,
	    data: formData,
	    dataType: "json",
	    processData: false,
    	contentType: false,
		headers: {
	      	"X-Requested-With": "XMLHttpRequest",
	      	"X-CSRFToken": $.cookie("csrftoken"),
	    },
	    success: (response) => {
	    	if (response["success"] && type == "donation") {
	    		window.location.href = response["url"]
	    	} else if (response["success"] && type == "volunteering") {
				alert("Спасибо за помощь");
		    	window.location.hash = "#";
	    	} else {
		    	alert("Что то пошло не так");
		    	window.location.hash = "#";
	    	}
	    }
  })
}


$("#donate-form").submit(function(event) {
	var amount = $("#id_donation_amount").val()
	var first_name = $("#id_donation_first_name").val()
	var last_name = $("#id_donation_last_name").val()
	var phone_number = $("#id_donation_phone_number").val()

	if (last_name != "" && first_name != "" && phone_number != "" && amount != "") {
		var formData = new FormData();

		formData.append("amount", amount);
		formData.append("first_name", first_name);
		formData.append("last_name", last_name);
		formData.append("phone_number", phone_number);
	
		submit_request("donate", formData, "donation");
	} else {
		alert("Заполните все поля");
	}

	event.preventDefault();
})

$("#volunteer-form").submit(function(event) {
	var last_name = $("#id_last_name").val();
	var first_name = $("#id_first_name").val();
	var phone_number = $(".phone_number").val();

	if (last_name != "" && first_name != "" && phone_number != "") {
		var formData = new FormData();
		
		formData.append("last_name", last_name);
		formData.append("first_name", first_name);
		formData.append("phone_number", phone_number);

		submit_request("to_be_volunteer", formData, "volunteering");
	} else {
		alert("Заполните все поля");
	}
	
	event.preventDefault();
})