$("#login-form").submit(function(event) {
	var formData = new FormData();
	
	formData.append("username", $("#id-login-username").val());
	formData.append("password", $("#id-login-password").val());

	$.ajax({
	    type: "POST",
	    url: `/authorization/login/`,
	    data: formData,
	    dataType: "json",
	    processData: false,
    	contentType: false,
		headers: {
		    "X-Requested-With": "XMLHttpRequest",
		    "X-CSRFToken": $.cookie("csrftoken"),
	    },
	    complete: (xhr, textStatus) => {
	    	if (xhr.responseText.includes("userProfile") || xhr.responseText.includes("admin")) {
	    		window.location.href = "/profile/";
	    	} else {
	    		alert("Enter valid login data");
	    	}
	    }
  	})

	event.preventDefault();
})


$("#sign-up-form").submit(function(event) {
	var formData = new FormData();
	
	formData.append("username", $("#id-sign-up-username").val());
	formData.append("first_name", $("#id-sign-up-first-name").val());
	formData.append("last_name", $("#id-sign-up-last-name").val());
	formData.append("phone_number", $("#id-sign-up-phone-number").val());
	formData.append("password1", $("#id-sign-up-password1").val());
	formData.append("password2", $("#id-sign-up-password2").val());

	$.ajax({
	    type: "POST",
	    url: `/authorization/sign-up/`,
	    data: formData,
	    dataType: "json",
	    processData: false,
    	contentType: false,
		headers: {
		    "X-Requested-With": "XMLHttpRequest",
		    "X-CSRFToken": $.cookie("csrftoken"),
	    },
	    success: (response) => {
	    	if (response["success"]) {
	    		alert("You are successfully registered, so you can login");
	    		window.location.hash = "log-zatemnenie";
	    	} else {
	    		errors = response["errors"];
	    		text = "";
	    		Object.keys(errors).forEach((key) => {
					for (var i = 0; i < errors[key].length; i++) {
		    			text += `* ${errors[key][i]}\n`;
		    		}
	    		});
	    		alert(text);
	    	}
	    },
	    error: (error) => {
	    	console.log(error);
	    }
  	})

	event.preventDefault();
})