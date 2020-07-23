document.addEventListener('DOMContentLoaded',function(){

  function getCookie(name){
    var cookieValue = null;
    if (document.cookie && document.cookie !== ''){
      var cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++){
        var cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + '=')){
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
    let field = document.getElementById('id_password');
    field.value = field.defaultValue;
    let cfield = document.getElementById('passwordcheck');
    cfield.value= cfield.defaultValue;
    }
});

function myfunction(csrftoken){
  let input = document.getElementById('id_username');
  $.ajax({
    headers: { "X-CSRFToken": csrftoken },
    url : "/check_username", // the endpoint
    type : "POST", // http method
    data : { the_post : input.value },
    success: function(data){
    if(data){
      document.getElementById("taken").innerHTML = "That username is taken";
      var field = document.getElementById('id_username');
      field.value= field.defaultValue;
      }
    else{
      document.getElementById("form").submit();
      }
    }
   });
 };


});
