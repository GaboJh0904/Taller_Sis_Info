

INSERT INTO `planificacion_inventario`.`empleado` (`ID`, `NOMBRE`, `ROL`, `TELFONO`, `FECHA_REGISTRO`) VALUES ('1', 'Juan Perez', 'Admin', '80803356', '2024-09-01');

INSERT INTO `planificacion_inventario`.`usuario` (`ID`, `PASSWOR_HASH`, `USER_NAME`, `EMAIL`, `EMPLEADO_ID`) VALUES ('1', '$2a$12$1mHoKIOnfZ7LcEi6/8SgC.RD1ogm8MBeSfSk.3cbPve/8N21pVbmO', 'JuanPerez', 'juanperez@gmail.com', '1');



INSERT INTO `planificacion_inventario`.`material` (`ID`, `NOMBRE`, `DESCRIPCION`, `CANTIDAD`, `PRECIO_UNITARIO`, `CANTIDAD_MINIMA`) VALUES ('1', 'Cemento', 'Polvo', '100', '10', '20');


