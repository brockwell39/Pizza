document.addEventListener('DOMContentLoaded',function(){

  document.getElementById('confirm').addEventListener("click", function(event){
    event.preventDefault();
    let x = document.getElementById("asap").checked;
    let y = document.getElementById("time").value;
    if ((x == false && y == "") || (x == true && y != "")){
      document.getElementById('asaptime').innerHTML = "Please select either ASAP or a time";
      document.getElementById('time').value = "";
      document.getElementById('asap').checked = false;
    }
    else {
    document.getElementById('timeform').submit();
    }
  })
});
