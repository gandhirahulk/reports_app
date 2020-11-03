$(document).ready(function(){
    var toggler = document.getElementsByClassName("treebox");
    var i;

    for (i = 0; i < toggler.length; i++) {
        toggler[i].addEventListener("click", function() {
        this.parentElement.querySelector(".nested").classList.toggle("activetree");
        this.classList.toggle("check-box");
        });
    }

    $("#menuone").on("click", function(){
        if (this.checked) { 
            empcheckboxes = document.getElementsByName('menuone');
            for(var i=0, n=empcheckboxes.length;i<n;i++) {
            empcheckboxes[i].checked = true;
            }
        }else {
            empcheckboxes = document.getElementsByName('menuone');
            for(var i=0, n=empcheckboxes.length;i<n;i++) {
            empcheckboxes[i].checked = false;
            }
        }
    });
    $(".eachmenuoneselect").on("click", function(){
        allcheckboxes = document.getElementsByName('menuone');
        if (this.checked) { 
            var checked = 0;
            for(var i=0, n=allcheckboxes.length;i<n;i++) {
            if (allcheckboxes[i].checked == true){
                checked += 1;
                }
            }
            if (checked === n){
            selectallcheckbox = document.getElementById('menuone');
            selectallcheckbox.checked = true;
                }
        }else {
            selectallcheckbox = document.getElementById('menuone');
            selectallcheckbox.checked = false;
        }
    });
    $("#menuoneone").on("click", function(){
        if (this.checked) { 
            empcheckboxes = document.getElementsByName('menuoneone');
            for(var i=0, n=empcheckboxes.length;i<n;i++) {
            empcheckboxes[i].checked = true;
            }
        }else {
            empcheckboxes = document.getElementsByName('menuoneone');
            for(var i=0, n=empcheckboxes.length;i<n;i++) {
            empcheckboxes[i].checked = false;
            }
        }
    });
    $(".eachmenuoneoneselect").on("click", function(){
        allcheckboxes = document.getElementsByName('menuoneone');
        if (this.checked) { 
            var checked = 0;
            for(var i=0, n=allcheckboxes.length;i<n;i++) {
            if (allcheckboxes[i].checked == true){
                checked += 1;
                }
            }
            if (checked === n){
            selectallcheckbox = document.getElementById('menuoneone');
            selectallcheckbox.checked = true;
                }
        }else {
            selectallcheckbox = document.getElementById('menuone');
            selectallcheckbox.checked = false;
        }
    });
    $("#menuonetwo").on("click", function(){
        if (this.checked) { 
            empcheckboxes = document.getElementsByName('menuonetwo');
            for(var i=0, n=empcheckboxes.length;i<n;i++) {
            empcheckboxes[i].checked = true;
            }
        }else {
            empcheckboxes = document.getElementsByName('menuonetwo');
            for(var i=0, n=empcheckboxes.length;i<n;i++) {
            empcheckboxes[i].checked = false;
            }
        }
    });
    $(".eachmenuonetwoselect").on("click", function(){
        allcheckboxes = document.getElementsByName('menuonetwo');
        if (this.checked) { 
            var checked = 0;
            for(var i=0, n=allcheckboxes.length;i<n;i++) {
            if (allcheckboxes[i].checked == true){
                checked += 1;
                }
            }
            if (checked === n){
            selectallcheckbox = document.getElementById('menuonetwo');
            selectallcheckbox.checked = true;
                }
        }else {
            selectallcheckbox = document.getElementById('menuonetwo');
            selectallcheckbox.checked = false;
        }
    });
    $("#menuonethree").on("click", function(){
        if (this.checked) { 
            empcheckboxes = document.getElementsByName('menuonethree');
            for(var i=0, n=empcheckboxes.length;i<n;i++) {
            empcheckboxes[i].checked = true;
            }
        }else {
            empcheckboxes = document.getElementsByName('menuonethree');
            for(var i=0, n=empcheckboxes.length;i<n;i++) {
            empcheckboxes[i].checked = false;
            }
        }
    });
    $(".eachmenuonethreeselect").on("click", function(){
        allcheckboxes = document.getElementsByName('menuonethree');
        if (this.checked) { 
            var checked = 0;
            for(var i=0, n=allcheckboxes.length;i<n;i++) {
            if (allcheckboxes[i].checked == true){
                checked += 1;
                }
            }
            if (checked === n){
            selectallcheckbox = document.getElementById('menuonethree');
            selectallcheckbox.checked = true;
                }
        }else {
            selectallcheckbox = document.getElementById('menuonethree');
            selectallcheckbox.checked = false;
        }
    });
});