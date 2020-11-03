function validate(element_id) {
    let element = document.getElementById(element_id);
    let name = element.name;
    let max_length = document.getElementById(element_id).maxLength;
    let min_length = document.getElementById(element_id).minLength;

    if (!validate_pattern(element.value, element_id)) {
        set_error(element_id, element.value.slice(-1) + " is not a valid character");
    } else if (element.value.trim() === null) {
        set_error(element_id, name + " cannot be blank");
    } else if (element.value.length == max_length && !validate_full_length_value(element.value, element_id)) {
        set_length_error(element_id, "Invalid value");
    } else if (element.value.length < min_length) {
        set_length_error(element_id, "entered value cannot be less than " + min_length.toString());
    } else if (element.value.length > max_length) {
        set_length_error(element_id, "entered value cannot be greater than " + max_length.toString());
    } else {
        set_success(element_id);
    }
}

function validate_full(textbox){
    if (!validate_full_length_value(textbox.value,textbox.id)) {
        textbox.setCustomValidity('Please provide a valid value!');
    }
}

function validate_full_length_value(input, id) {
    let fieldToPatternMap = new Map();
    fieldToPatternMap.set("firstname", /^[a-zA-Z]+(([.\s][a-zA-Z])?[a-zA-Z]*)*$/);
    fieldToPatternMap.set("firstname", /^[a-zA-Z]+(([.\s][a-zA-Z])?[a-zA-Z]*)*$/);

    fieldToPatternMap.set("firstname", /^[a-zA-Z]+(([.\s][a-zA-Z])?[a-zA-Z]*)*$/);
    fieldToPatternMap.set("oemail", /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/);
    fieldToPatternMap.set("oemail", /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/);
    fieldToPatternMap.set("aadhaarCard", /^[1-9][0-9]{11}$/);
    fieldToPatternMap.set("panCard", /^[a-zA-Z]{4}[Pp][0-9]{4}[a-zA-Z]$/);
    fieldToPatternMap.set("voterCard", /^([a-zA-Z]){3}([0-9]){7}?$/);
    fieldToPatternMap.set("drivingLicense", /^(([a-zA-Z]{2}[0-9]{2})|([A-Z]{2}[0-9]{2}))((19|20)[0-9][0-9])[0-9]{7}$/);
    fieldToPatternMap.set("uanNumber", /^d{12}$/);
    fieldToPatternMap.set("passportNumber", /^[A-Za-z][1-9][0-9]{6}$/);
    fieldToPatternMap.set("companyemail", /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/);
    // fieldToPatternMap.set("companypassword", /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/);

    if (id.includes('--')) {
        id = id.split('--')[0]
    }
    if (fieldToPatternMap.has(id)) {
        console.log(input)
        return fieldToPatternMap.get(id).test(input);
    }
    else {
        alert(id);
    }

}

function validate_pattern(input, id) {
    let fieldToPatternMap = new Map();
    fieldToPatternMap.set("employeecode", /^[a-zA-Z0-9]{0,8}$/);
    fieldToPatternMap.set("firstname", /^[a-zA-Z.\s]{0,30}$/);
    // fieldToPatternMap.set("firstname", /^[a-zA-Z]+(([.\s][a-zA-Z])?[a-zA-Z]*)*$/);
    fieldToPatternMap.set("middlename", /^[a-zA-Z.\s]{0,30}$/);
    fieldToPatternMap.set("lastname", /^[a-zA-Z.\s]{0,30}$/);
    // fieldToPatternMap.set("oemail", /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/);
    // fieldToPatternMap.set("oemail", /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/);
    // fieldToPatternMap.set("pemail", /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/);
    fieldToPatternMap.set("mobile", /^[\d]{0,10}$/);
    fieldToPatternMap.set("amob", /^[\d]{0,10}$/);
    fieldToPatternMap.set("rmcode", /^[a-zA-Z0-9]{2,8}$/);
    fieldToPatternMap.set("peraddress", /^[a-zA-Z0-9#',.\-\\\/ ](?!.* {2})[a-zA-Z0-9#',.\-\\\/ ]{0,100}$/);
    fieldToPatternMap.set("curaddress", /^[a-zA-Z0-9#',.\-\\\/ ](?!.* {2})[a-zA-Z0-9#',.\-\\\/ ]{0,100}$/);
    fieldToPatternMap.set("perpin", /^[1-9]{0,1}[0-9]{1,5}$/);
    fieldToPatternMap.set("curpin", /^[1-9]{0,1}[0-9]{1,5}$/);
    fieldToPatternMap.set("religion", /^[a-zA-Z\s]+$/);
    fieldToPatternMap.set("aadhaarCard", /^[1-9]{0,1}[0-9]{0,11}$/);
    fieldToPatternMap.set("panCard", /^[A-Za-z0-9]{0,10}$/);
    fieldToPatternMap.set("voterCard", /^[a-zA-Z0-9]{0,10}$/);
    fieldToPatternMap.set("drivingLicense", /^[a-zA-Z0-9]{0,15}$/);
    fieldToPatternMap.set("uanNumber", /^[0-9]{0,12}$/);
    fieldToPatternMap.set("passportNumber", /^[A-Za-z0-9]{0,8}$/);
    fieldToPatternMap.set("mothername", /^[a-zA-Z.\s]{0,30}$/);
    fieldToPatternMap.set("fathername", /^[a-zA-Z.\s]{0,30}$/);
    fieldToPatternMap.set("spousename", /^[a-zA-Z.\s]{0,30}$/);
    fieldToPatternMap.set("childname", /^[a-zA-Z.\s]{0,30}$/);
    fieldToPatternMap.set("school", /^[a-zA-Z0-9-.,\s]+$/);
    fieldToPatternMap.set("university", /^[a-zA-Z0-9-.,\s]+$/);
    fieldToPatternMap.set("grade", /^10(\.0{0,2}?)?$|^\d?(\.\d{0,2})?$/);
    fieldToPatternMap.set("percentage", /^100(\.0{0,2}?)?$|^\d{0,2}(\.\d{0,2})?$/);
    fieldToPatternMap.set("companyName", /^[a-zA-Z0-9-.\s]+$/);
    fieldToPatternMap.set("designation", /^[a-zA-Z0-9-.\s]+$/);
    fieldToPatternMap.set("jobRole", /^[a-zA-Z0-9-,.\s]+$/);
    fieldToPatternMap.set("ctc", /^\d{0,10}$/);
    fieldToPatternMap.set("exp", /^(0?[1-9]|1[012])$/);
    //ORGANIZATION
    let name_regex = /^[a-zA-Z0-9.\s](?!.* {2})[a-zA-Z0-9.\s]{0,100}$/
    fieldToPatternMap.set('companyname', name_regex)
    fieldToPatternMap.set('group',name_regex)
    fieldToPatternMap.set('team',name_regex)
    fieldToPatternMap.set('vendor', name_regex)
    fieldToPatternMap.set('business', name_regex)
    fieldToPatternMap.set('function', name_regex)
    fieldToPatternMap.set('sub_function', name_regex)
    fieldToPatternMap.set('role', name_regex)
    fieldToPatternMap.set('designation', name_regex)
    fieldToPatternMap.set('regionname', name_regex)
    fieldToPatternMap.set('statename', name_regex)
    fieldToPatternMap.set('locationname', name_regex)
    fieldToPatternMap.set('sublocationname', name_regex)
    fieldToPatternMap.set("sublocationaddress", /^[a-zA-Z0-9#',.\-\\\/ ](?!.* {2})[a-zA-Z0-9#',.\-\\\/ ]{0,100}$/)
    fieldToPatternMap.set('gendername', /^[a-zA-Z\-\s](?!.* {2})[ \w.-]{0,30}$/)
    fieldToPatternMap.set('companyaddress', /^[a-zA-Z0-9#',.\-\\\/ ](?!.* {2})[a-zA-Z0-9#',.\-\\\/ ]{0,100}$/)
    fieldToPatternMap.set('companyphone', /^[\d]{0,10}$/)
    fieldToPatternMap.set('contactperson',  /^[a-zA-Z.\s](?!.* {2})[a-zA-Z.\s]{0,30}$/)
    fieldToPatternMap.set('companylocation',  /^[a-zA-Z ](?!.* {2})[a-zA-Z ]{0,100}$/)
    fieldToPatternMap.set('companywebsiteurl', /^[A-Za-z0-9.:/\s](?!.* {2})[A-Za-z0-9_.:/\s]{0,100}$/)
    fieldToPatternMap.set('companyemail', /^[A-Za-z0-9._@]{0,100}$/)
    fieldToPatternMap.set('companyserver',  /^[a-zA-Z0-9.](?!.* {2})[a-zA-Z0-9.]{0,100}$/)
    fieldToPatternMap.set('companyport', /^[0-9]{0,4}$/)

    if (id.includes('--')) {
        id = id.split('--')[0]
    }
    if (fieldToPatternMap.has(id)) {
        return fieldToPatternMap.get(id).test(input);
    }
    else {
        alert(id);
    }
}

function set_error(id, message) {
    let inputElement = document.getElementById(id);
    let parentElement = inputElement.parentNode;
    const small = parentElement.querySelector('small');
    let input_text = document.getElementById(id).value;
    document.getElementById(id).value = input_text.substring(0, input_text.length - 1)
    small.innerText = message;
    small.style.display = 'block';
    parentElement.className = 'box error';
}

function set_success(id) {
    let inputElement = document.getElementById(id);
    let parentElement = inputElement.parentNode;
    const small = parentElement.querySelector('small');
    small.style.display = 'none';
    parentElement.className = 'box success';
}

function set_length_error(element_id, message) {
    let inputElement = document.getElementById(element_id);
    let parentElement = inputElement.parentNode;
    const small = parentElement.querySelector('small');
    small.innerText = message;
    small.style.display = 'block';
    parentElement.className = 'box error';
}

function validate_organization(textbox) {
    if (textbox.value === '') {
        textbox.setCustomValidity('Invalid input !');
    } else if (textbox.validity.typeMismatch) {
        textbox.setCustomValidity('Invalid input !');
    } else if (!validate_pattern(textbox.value, textbox.id)) {
        textbox.setCustomValidity('Invalid input !');
        textbox.value = textbox.value.substring(0, textbox.value.length - 1)
    } else {
        textbox.setCustomValidity('');
    }
    return true;
}


function validate_email(textbox) {
    if (textbox.value === '') {
        textbox.setCustomValidity('Please provide Company Email ID');
    } else if (textbox.validity.typeMismatch) {
        textbox.setCustomValidity('Please provide valid Email ID!');
    } else {
        textbox.setCustomValidity('');
    }
    return true;
}

function check_for_errors() {
    var msgs = document.getElementById('msgfromdjango')
    var company_form = document.getElementById("create_company_form");
    console.log(msgs)

    if (msgs != "") {
        console.log('in if loop')
        document.getElementById("sidebar").style.zIndex = "-1";
        company_form.style.display = "block";
    }
}

function validate_coordinates(textbox) {
    let id = textbox.id
    let lat_long_regex = /^[+\-0-9.]{0,10}$/
    let fieldToPatternMap = new Map();
    fieldToPatternMap.set('latitude', lat_long_regex)
    fieldToPatternMap.set('longitude', lat_long_regex)
    fieldToPatternMap.set('radius', /^[0-9.]{0,10}$/)
    if (id.includes('--')) {
        id = id.split('--')[0]
    }

    if (fieldToPatternMap.has(id)) {
        if(!fieldToPatternMap.get(id).test(textbox.value)){
            console.log(textbox.value.substring(0, textbox.value.length - 1))
            textbox.value = textbox.value.substring(0, textbox.value.length - 1)
            textbox.setCustomValidity('Invalid input !');
        }
        else {
            textbox.setCustomValidity('');
        }
    }
    return true;
}
function validate_coordinates_full_length(textbox) {
    let lat_long_regex = /^(\+|-)?(?:90(?:(?:\.0{1,6})?)|(?:[0-9]|[1-8][0-9])(?:(?:\.[0-9]{1,6})?))$/
    if (textbox.validity.typeMismatch) {
        textbox.setCustomValidity('Invalid input !');
    } else if (!lat_long_regex.test(textbox.value)) {
        textbox.setCustomValidity('Invalid input !');
    } else {
        textbox.setCustomValidity('');
    }
}

