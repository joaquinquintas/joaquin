<?php
$remitente = $_POST['email'];
//$remitente = 'energia@sustentator.com'; // pruebo desde aca ALX
$destinatario = 'energiasustentator@gmail.com, energia@sustentator.com'; // en esta línea va el mail del destinatario, puede ser una cuenta de hotmail, yahoo, gmail, etc
//$IP = $_SERVER['SERVER_ADDR']; // Get IP
$energia = $_POST["energia"];
$provincia = $_POST["provincia"];

if (!$_POST){
?>

<?php
}else{
	//abro la base
	$con=mysqli_connect("dbase.sustentator.com","energia","405fle405","energia");
	// Check si abrio o no
	if (mysqli_connect_errno()) {
		echo "Failed to connect to MySQL: " . mysqli_connect_error();
	}
	// HACK TRUCHO para dump el CSV
	if ($remitente == 'home@space.ibiza'){
		$result = $con->query('SELECT * FROM `contactos`');
		if (!$result) die('Couldn\'t fetch records');
		$num_fields = mysql_num_fields($result);
		$headers = array();
		for ($i = 0; $i < $num_fields; $i++) {
		$headers[] = mysql_field_name($result , $i);
		}
		$fp = fopen('php://output', 'w');
		if ($fp && $result) {
			header('Content-Type: text/csv');
			header('Content-Disposition: attachment; filename="'.date('Y-m-d').'-export.csv"');
			header('Pragma: no-cache');
			header('Expires: 0');
			fputcsv($fp, $headers);
			while ($row = $result->fetch_array(MYSQLI_NUM)) {
				fputcsv($fp, array_values($row));
			}
		die;
		}
	}
	else

	//$cuerpo  = "Enviado a  : " . $_POST["mail_to"] . "\r\n"; a
    //$cuerpo .= "Server     : " . $IP . "\r\n";
	$cuerpo  = "Enviado de : " . $_POST["email"] . "\r\n";
	$cuerpo  = "Enviado Por : " . $_POST["first_name"] . "\r\n";
	$cuerpo .= "Celular    : " . $_POST["telephone"] . "\r\n";
	$cuerpo .= "IP Cliente : " . $_SERVER['REMOTE_ADDR'] . "\r\n\r\n";
	$cuerpo .= "Provincia  : " . $provincia . "\r\n";
	$cuerpo .= "Energia    : " . $energia . "\r\n";
	$cuerpo .= "Consulta   : " . $_POST["comments"] . "\r\n";
	//las líneas de arriba definen el contenido del mail. Las palabras que están dentro de $_POST[""] deben coincidir con el "name" de cada campo. 
	// Si se agrega un campo al formulario, hay que agregarlo acá.

	//ESTO LIMPIA LOS CAMPOS PARA EVITAR SQL_INJECTION - NO SACAR NUNCA !
	$email = mysqli_real_escape_string($con, $_POST['email']);
	$tel = mysqli_real_escape_string($con, $_POST['telephone']);
	$provincia = mysqli_real_escape_string($con, $_POST['provincia']);
	$energia = mysqli_real_escape_string($con, $_POST['energia']);
	$comments = mysqli_real_escape_string($con, $_POST['comments']);
	$ip = mysqli_real_escape_string($con, $_SERVER['REMOTE_ADDR']);
	$name = mysqli_real_escape_string($con, $_POST["first_name"]);

	$sql=	"INSERT INTO contactos (email, name, tel, provincia, energia, comments, ip)
			VALUES ('$email', '$name','$tel', '$provincia', '$energia', '$comments', '$ip')";

	if (!mysqli_query($con,$sql)) {
	  die('Error: ' . mysqli_error($con));
	}
	$id = mysqli_insert_id($con);
	//echo "1 record added No:". mysqli_insert_id($con) ;
		
	mysqli_close($con);
	
	$asunto = 'S//E -id: '.$id.' -'.$provincia.'-'.$energia; // acá se puede modificar el asunto del mail
	
    $headers  = "MIME-Version: 1.0\n";
    $headers .= "Content-type: text/plain; charset=utf-8\n";
    $headers .= "X-Priority: 3\n";
    $headers .= "X-MSMail-Priority: Normal\n";
    $headers .= "X-Mailer: php\n";
	
	// MAIL 1 :
    $headers_1 = $headers . "From: \"".$_POST['first_name']." ".$_POST['email']."\" <".$remitente.">\n";
    mail($destinatario, $asunto, $cuerpo, $headers_1);
	// \1
	
	// MAIL 2 :
	$remitente = 'energia@sustentator.com'; // pruebo desde aca ALX
	$asunto_2 = 'S//E - BKP - de:'.$_POST['email'].'-'.$provincia.' - '.$energia; 
	$headers_2 = $headers . "From: \"".$_POST['email']."\" <".$remitente.">\n";
	$headers_2 .= "Sender: energia@sustentator.com\n";
	$headers_2 .= "Reply-to:".$_POST['email']."\n";
    mail($destinatario, $asunto_2, $cuerpo, $headers_2);
    // \2
	
	include '../confirma.html'; //se debe crear un html que confirma el envío
}
?>
