<?php

// *******************************
// VII Pylestras - Diversão e lucro com Raspberry Pi
// dezembro de 2014
// *******************************

if (isset($_POST["codigo"])) {
	send_UDP($_POST["codigo"]);
}

// Função de envio via UDP
function send_UDP($data){
$server = 'localhost';
$port = 8888;

	if(!($sock = socket_create(AF_INET, SOCK_DGRAM, 0)))
	{
		$errorcode = socket_last_error();
		$errormsg = socket_strerror($errorcode);  
		die("Erro ao criar socket: [$errorcode] $errormsg <br>");
	}else{
		echo "Socket criado na porta: $port <br>";
		if(!socket_sendto($sock, $data , strlen($data) , 0 , $server , $port))
			{
			  $errorcode = socket_last_error();
			  $errormsg = socket_strerror($errorcode);
			  die("Não foi possível enviar: [$errorcode] $errormsg  <br>");
			  exit();
			} 
	}
}	
?>

<!DOCTYPE html>
<html>
<head>
	<title>WEB MISSILE</title>
	<script type='text/javascript'  src="jquery-2.1.1.min.js"></script>
	<script type="text/javascript">
	 
	function getKeyCode(e) {
	    $.post('index.php', {
	    	codigo: e.keyCode
	    },function(data) {
		});
	}
	</script>
</head>

<body onkeydown="getKeyCode(event);" bgcolor="gray">
	<img src="http://192.168.1.4:8081"><br>
	<p>Pressione uma tecla...<br>
	<img src="Arrow-keys.jpg">
	</p>
</body>
</html>

















''