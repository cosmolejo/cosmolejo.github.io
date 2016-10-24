<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<?php
        /////////////////////////////////////////////////
        //VARIABLES DE ENTRADA
        /////////////////////////////////////////////////
        if(isset($_GET["color"]))
        {
            $color=$_GET["color"];
            $densidadmin=$_GET["densidadmin"];
        }
        else
        {
            $color="gray";
            $densidadmin=0;
        }
?>
<html>
    <head>
      <meta content="text/html; charset=ISO-8859-1" http-equiv="content-type">
      <title>tabla periodica</title>
    </head>
    <body>
        <center>
            <h1>Tabla periodica</h1>
        </center>
	
	<form action="tabla.php">
            Color:
            <input type="text" name="color" value="<?php echo $color ?>"/>
            Densidad mínima:
            <input type="text" name="densidadmin" value="<?php echo $densidadmin?>"/>
            <input type="submit" name="boton" value="Cambiar color"/>
            <br>
        </form>
        
        <form action="tabla.php" method="post">
            <p>Imprimir (elimina los colores): </p>
            <input type="checkbox" name="peso" value="T" <?php if(isset($_POST['peso'])) echo "checked='checked'"; ?> > peso atómico<br>
            <input type="checkbox" name="densidad" value="T"<?php if(isset($_POST['densidad'])) echo "checked='checked'"; ?>  > densidad<br>
            <input type="checkbox" name="fusión" value="T"?<?php if(isset($_POST['fusión'])) echo "checked='checked'"; ?> > punto de fusión<br>
            <input type="checkbox" name="ebullición" value="T"<?php if(isset($_POST['ebullición'])) echo "checked='checked'"; ?>> punto de ebullición<br>
            <input type="submit" value="enviar">
         </form>
    <br>
        <table border=1px style='border-collapse: collapse;border:solid black 0px;'>
            <center>
            <?php
                ////////////////////////////////////////////////////////////////
                // LECTURA DEL FORMULARIO
                ////////////////////////////////////////////////////////////////
                function Check($chkname,$value)
                {
                    if(!empty($_POST[$chkname]))
                    {
                        foreach($_POST[$chkname] as $chkval)
                        {
                            if($chkval == $value)
                            {
                                return true;
                            }
                        }
                    }
                    return false;
                }
            
            
                $aux=  array(A,B,C,D);
                $elements = array(); //arreglo del archivo
                $file = fopen("ElementosQuimicos.txt", "r");
                while (!feof($file) )
                {
                    $line = fgets($file);
                    $elements[] = explode(',', $line);
                }

                fclose($file);
                 
                $blancos=array
                        (
                            "0"=>array(),
                            "1"=>array(2,17),
                            "2"=>array(3,12),
                            "3"=>array(3,12),
                            "4"=>array(0,0),
                            "5"=>array(0,0),
                            "6"=>array(0,0),
                            "7"=>array(0,0)
                        );

                $Z=0;
                
                for($i=1;$i<=7;$i++)
                {
                    echo "<tr>";
                    $limites=$blancos[$i];
                    $minimo=$limites[0];
                    $maximo=$limites[1];
                    for($j=1;$j<=18;$j++)
                    {
                        if($j<$minimo or $j>$maximo)
                            {
                                $dens=  array();
                                $Z++;
                                $simbolo=$elements[$Z][1];
                                $nombre=$elements[$Z][0];
                                preg_match("/(\d+\.\d+).+/",$elements[$Z][4],$m);
                                $densidad=$m[1];
                                $aux[]=$densidad;
                                
                                if($densidad<$densidadmin)
                                {
                                    $colornuevo="white";
                                }
                                else
                                {
                                    $colornuevo=$color;
                                }
                                echo 
                                "
                                    <td style='border:solid black 1px;font-size:0.8em; background:$colornuevo;'>
                                        <div style='float:right'>$Z</div>
                                        <big>$simbolo</big><br/>
                                        $nombre <br> 
                                ";
                                if(isset($_POST['peso']) && $_POST['peso'] == 'T') 
                                {
                                    $peso=$elements[$Z][3];
                                    echo "$peso <br> ";
                                }
                                if(isset($_POST['densidad']) && $_POST['densidad'] == 'T') 
                                {
                                    //$peso=$elements[$Z][3];
                                    echo "$densidad <br> ";
                                }
                                if(isset($_POST['fusión']) && $_POST['fusión'] == 'T') 
                                {
                                    $fus=$elements[$Z][5];
                                    echo "$fus <br> ";
                                }
                                if(isset($_POST['ebullición']) && $_POST['ebullición'] == 'T') 
                                {
                                    $ebu=$elements[$Z][6];
                                    echo "$ebu <br> ";
                                }
                                echo "</td>";
                                /*
                                $x=3;
                                $topics = $_POST['topic'];
                                if(empty($topics)) 
                                {
                                    echo "</td>";  
                                } 
                                else
                                {
                                    $N = count($topics)+3;
                                    for($i=3; $i < $N; $i++)
                                    {
                                        $topico=$elements[$Z][$i];
                                        echo "$topico <br>";
                                            
                                    }
                                    echo "</td>";
                                }
                                
                                 */
                                
                            }
                            else
                            {
                                echo "<td style='border:solid black 0px;'></td>";
                            }
                    }
                    echo "</tr>";
                }     

            ?>
            </center>
        </table>
    </body>
</html>
