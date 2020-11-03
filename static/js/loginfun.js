function disFun() {
    if(document.getElementById('username').value==="" || document.getElementById('Password').value==="") { 
            document.getElementById('btn').disabled = true; 
        } else { 
            document.getElementById('btn').disabled = false;
        }
}
function disFunForForgot() {
    if(document.getElementById('empcode').value==="") { 
            document.getElementById('send-btn').disabled = true; 
        } else { 
            document.getElementById('send-btn').disabled = false;
        }
}

