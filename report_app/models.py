from django.db import models


class status(models.Model):
    pk_status_code = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=100)

    created_by = models.CharField(max_length=100)
    created_date_time = models.DateTimeField(auto_now_add=True, blank=True)
    modified_by = models.CharField(max_length=100, null=True, blank=True)
    modified_date_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.status_name

class gender(models.Model):
    pk_gender = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    created_by = models.CharField(max_length=100)
    created_date_time = models.DateTimeField(auto_now_add=True, blank=True)
    modified_by = models.CharField(max_length=100, null=True, blank=True)
    modified_date_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.ForeignKey(status, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class template_variables(models.Model):
    pk_field_code = models.AutoField(primary_key=True)
    field_name = models.CharField(max_length=100)
    db_table_name = models.CharField(max_length=100)
    sort_column = models.CharField(max_length=100, default='name')

    created_by = models.CharField(max_length=100)
    created_date_time = models.DateTimeField(auto_now_add=True, blank=True)
    modified_by = models.CharField(max_length=100, null=True, blank=True)
    modified_date_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.field_name


class designation(models.Model):
    pk_designation = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    created_by = models.CharField(max_length=100)
    created_date_time = models.DateTimeField(auto_now_add=True, null=True)
    modified_by = models.CharField(max_length=100, null=True, blank=True)
    modified_date_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.ForeignKey(status, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name

class region(models.Model):
    pk_region = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    created_by = models.CharField(max_length=100)
    created_date_time = models.DateTimeField(auto_now_add=True, null=True)
    modified_by = models.CharField(max_length=100, null=True, blank=True)
    modified_date_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.ForeignKey(status, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name


class department(models.Model):
    pk_department = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    created_by = models.CharField(max_length=100)
    created_date_time = models.DateTimeField(auto_now_add=True, blank=True)
    modified_by = models.CharField(max_length=100, null=True, blank=True)
    modified_date_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.ForeignKey(status, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name


class function_category(models.Model):
    pk_function_category = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    department = models.ForeignKey(department, on_delete=models.CASCADE, null=True)

    created_by = models.CharField(max_length=100)
    created_date_time = models.DateTimeField(auto_now_add=True, blank=True)
    modified_by = models.CharField(max_length=100, null=True, blank=True)
    modified_date_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.ForeignKey(status, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name


class team(models.Model):
    pk_team = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    function_category = models.ForeignKey(function_category, on_delete=models.CASCADE, null=True)

    created_by = models.CharField(max_length=100)
    created_date_time = models.DateTimeField(auto_now_add=True, blank=True)
    modified_by = models.CharField(max_length=100, null=True, blank=True)
    modified_date_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.ForeignKey(status, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name

class ctc_slab(models.Model):
    pk_ctc = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    created_by = models.CharField(max_length=100,null=True)
    created_date_time = models.DateTimeField(auto_now_add=True,null=True)
    modified_by = models.CharField(max_length=100, null=True)
    modified_date_time = models.DateTimeField(auto_now_add=True, null=True)
    status = models.ForeignKey(status, on_delete=models.CASCADE, null=True,default=2)

    def __str__(self):
        return self.name


class age(models.Model):
    pk_age = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    created_by = models.CharField(max_length=100,null=True)
    created_date_time = models.DateTimeField(auto_now_add=True,null=True)
    modified_by = models.CharField(max_length=100, null=True)
    modified_date_time = models.DateTimeField(auto_now_add=True, null=True)
    status = models.ForeignKey(status, on_delete=models.CASCADE, null=True,default=2)

    def __str__(self):
        return self.name

class exit_type(models.Model):
    pk_exit_type = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    created_by = models.CharField(max_length=100,null=True)
    created_date_time = models.DateTimeField(auto_now_add=True,null=True)
    modified_by = models.CharField(max_length=100, null=True)
    modified_date_time = models.DateTimeField(auto_now_add=True, null=True)
    status = models.ForeignKey(status, on_delete=models.CASCADE, null=True,default=2)

    def __str__(self):
        return self.name

class tenure(models.Model):
    pk_tenure = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    created_by = models.CharField(max_length=100,null=True)
    created_date_time = models.DateTimeField(auto_now_add=True,null=True)
    modified_by = models.CharField(max_length=100, null=True)
    modified_date_time = models.DateTimeField(auto_now_add=True, null=True)
    status = models.ForeignKey(status, on_delete=models.CASCADE, null=True,default=2)

    def __str__(self):
        return self.name

class entity(models.Model):
    pk_entity = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    created_by = models.CharField(max_length=100,null=True)
    created_date_time = models.DateTimeField(auto_now_add=True,null=True)
    modified_by = models.CharField(max_length=100, null=True)
    modified_date_time = models.DateTimeField(auto_now_add=True, null=True)
    status = models.ForeignKey(status, on_delete=models.CASCADE, null=True,default=2)

    def __str__(self):
        return self.name


class employment_type(models.Model):
    pk_type = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    created_by = models.CharField(max_length=100,null=True)
    created_date_time = models.DateTimeField(auto_now_add=True,null=True)
    modified_by = models.CharField(max_length=100, null=True)
    modified_date_time = models.DateTimeField(auto_now_add=True, null=True)
    status = models.ForeignKey(status, on_delete=models.CASCADE, null=True,default=2)

    def __str__(self):
        return self.name





class sub_team(models.Model):
    pk_sub_team = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    team = models.ForeignKey(team, on_delete=models.CASCADE, null=True)

    created_by = models.CharField(max_length=100)
    created_date_time = models.DateTimeField(auto_now_add=True, blank=True)
    modified_by = models.CharField(max_length=100, null=True, blank=True)
    modified_date_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.ForeignKey(status, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name


class state(models.Model):
    pk_state = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    sub_team = models.ForeignKey(sub_team, on_delete=models.CASCADE, null=True)

    created_by = models.CharField(max_length=100)
    created_date_time = models.DateTimeField(auto_now_add=True, blank=True)
    modified_by = models.CharField(max_length=100, null=True, blank=True)
    modified_date_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.ForeignKey(status, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name


class city(models.Model):
    pk_city = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    state = models.ForeignKey(state, on_delete=models.CASCADE, null=True)

    created_by = models.CharField(max_length=100)
    created_date_time = models.DateTimeField(auto_now_add=True, blank=True)
    modified_by = models.CharField(max_length=100, null=True, blank=True)
    modified_date_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.ForeignKey(status, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name


class location(models.Model):
    pk_location = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    city = models.ForeignKey(city, on_delete=models.CASCADE, null=True)

    created_by = models.CharField(max_length=100)
    created_date_time = models.DateTimeField(auto_now_add=True, blank=True)
    modified_by = models.CharField(max_length=100, null=True, blank=True)
    modified_date_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.ForeignKey(status, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name


class vendor(models.Model):
    pk_vendor = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.ForeignKey(location, on_delete=models.CASCADE, null=True)

    created_by = models.CharField(max_length=100)
    created_date_time = models.DateTimeField(auto_now_add=True, blank=True)
    modified_by = models.CharField(max_length=100, null=True, blank=True)
    modified_date_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.ForeignKey(status, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name


class employee(models.Model):
    udaan_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=100)
    status = models.ForeignKey(status, on_delete=models.CASCADE, null=True)
    doj = models.DateField()
    lwd = models.DateField()
    designation = models.ForeignKey(designation, on_delete=models.CASCADE, null=True)

    # fk
    department = models.ForeignKey(department, on_delete=models.CASCADE, null=True)
    function_category = models.ForeignKey(function_category, on_delete=models.CASCADE, null=True)
    team = models.ForeignKey(team, on_delete=models.CASCADE, null=True)
    sub_team = models.ForeignKey(sub_team, on_delete=models.CASCADE, null=True)
    state = models.ForeignKey(state, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(city, on_delete=models.CASCADE, null=True)
    location = models.ForeignKey(location, on_delete=models.CASCADE, null=True)
    vendor = models.ForeignKey(vendor, on_delete=models.CASCADE, null=True)

    # manger details
    reporting_manager_1 = models.CharField(max_length=100)
    reporting_manager_2 = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=10)

    created_by = models.CharField(max_length=100)
    created_date_time = models.DateTimeField(auto_now_add=True, blank=True)
    modified_by = models.CharField(max_length=100, null=True, blank=True)
    modified_date_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.employee_name


class dimensions(models.Model):
    pk_dimension = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    fk_table = models.ForeignKey(template_variables, on_delete=models.CASCADE, null=True)

    created_by = models.CharField(max_length=100)
    created_date_time = models.DateTimeField(auto_now_add=True, blank=True)
    modified_by = models.CharField(max_length=100)
    modified_date_time = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.ForeignKey(status, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.name)


class frequency(models.Model):
    pk_frequency = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    created_by = models.CharField(max_length=100)
    created_date_time = models.DateTimeField(auto_now_add=True, blank=True)
    modified_by = models.CharField(max_length=100)
    modified_date_time = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.ForeignKey(status, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.name)


class report_type(models.Model):
    pk_type = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    status = models.ForeignKey(status, on_delete=models.CASCADE, default=1)
    created_by = models.CharField(max_length=100)
    created_date_time = models.DateTimeField(auto_now_add=True, blank=True)
    modified_by = models.CharField(max_length=100)
    modified_date_time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return str(self.name)
