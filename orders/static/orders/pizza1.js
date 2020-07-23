document.addEventListener('DOMContentLoaded',function(){


  document.getElementById('confirm').onclick = function(event){
    event.preventDefault();
    var x = document.getElementById("asap").checked;
    var y = document.getElementById("time").value;
    if ((x == false && y == "") || (x == true && y != ""))  {
      document.getElementById('asaptime').innerHTML = "Please select either ASAP or a time";
      document.getElementById('time').value = "";
      document.getElementById('asap').checked = false;
    }
    else {
    document.getElementById('timeform').submit();
    };

  };

  document.getElementByName("menu").addEventListener("click", function(event){
    alert("Play");
  });



function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


document.getElementById("ptest").addEventListener("click", function(event)
{
        event.preventDefault()
        var csrftoken = getCookie('csrftoken');
        let p = document.getElementById('id_password');
        let pcheck = document.getElementById('passwordcheck');
        if(p.value == pcheck.value){
          document.getElementById("passwordnomatch").innerHTML = "";
          myfunction(csrftoken);
        }
        else{
        document.getElementById("passwordnomatch").innerHTML = "Passwords do not match";
        let field = document.getElementById('passwordr');
        field.value= field.defaultValue;
        let cfield = document.getElementById('passwordcheck');
        cfield.value= cfield.defaultValue;
        }

});

document.getElementById("confirm").addEventListener("click", function(event)
{
        alert("loop entered")
        event.preventDefault()

});

document.getElementById("ptes").addEventListener("click", function(event)
{
        alert("loop entered")
        event.preventDefault()
        var csrftoken = getCookie('csrftoken');
        myfunction(csrftoken);

});


function myfunction(csrftoken)
            {
            alert("ajax entered");
            let input = document.getElementById('id_username');
            $.ajax({
            headers: { "X-CSRFToken": csrftoken },
            url : "/check_username", // the endpoint
            type : "POST", // http method
            data : { the_post : input.value },
            success: function(data){
              if(data){
                document.getElementById("taken").innerHTML = "That username is taken";
                var field = document.getElementById('usernamer');
                field.value= field.defaultValue;
              }
              else{
                document.getElementById("form").submit();
              }
            }// data sent with the post request
        });
    };



});



function test(elem){
  alert(elem.id);
};
