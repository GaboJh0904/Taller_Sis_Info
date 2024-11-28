use planificacion_inventario;

INSERT INTO EMPLEADO (NOMBRE, ROL, TELFONO, FECHA_REGISTRO) VALUES
('JuanPerez', 'Operario', '555-1234', 20230101),
('MariaGomez', 'Supervisor', '555-5678', 20230102),
('CarlosLopez', 'Analista', '555-9012', 20230103);


INSERT INTO USUARIO (PASSWOR_HASH, USER_NAME, EMAIL, EMPLEADO_ID) VALUES
('$2a$12$1mHoKIOnfZ7LcEi6/8SgC.RD1ogm8MBeSfSk.3cbPve/8N21pVbmO', 'JuanPerez', 'juan.perez@example.com', 1),
('$2a$12$1mHoKIOnfZ7LcEi6/8SgC.RD1ogm8MBeSfSk.3cbPve/8N21pVbmO', 'MariaGomez', 'maria.gomez@example.com', 2),
('$2a$12$1mHoKIOnfZ7LcEi6/8SgC.RD1ogm8MBeSfSk.3cbPve/8N21pVbmO', 'CarlosLopez', 'carlos.lopez@example.com', 3);



INSERT INTO ENCARGADO_ALMACEN (NIVEL_ACCESO, NOTIFICACIONES_ACTIVAS, EMPLEADO_ID) VALUES
('Alto', TRUE, 1),
('Medio', FALSE, 2);


INSERT INTO ENCARGADO_PROYECTO (USUARIO_ID) VALUES
(1),
(2);


INSERT INTO ENCARGADO_FINANZAS (USUARIO_ID) VALUES
(3),
(2);


INSERT INTO GERENTE_INVENTARIO (NIVEL_ACCESO, ENCARGADO_PEDIDOS, NOTIFICACIONES_ACTIVAS, USUARIO_ID) VALUES
('Alto', TRUE, TRUE, 1),
('Medio', FALSE, TRUE, 2);


INSERT INTO PROYECTO (
    NOMBRE, DESCRIPCION, CRONOGRAMA, PRESUPUESTO_ASIGNADO, METAS_FINANCIERAS, 
    ESTADO, PRIORIDAD, FECHA_INICIO, FECHA_FIN, 
    ENCARGADO_PROYECTO_ID, GERENTE_INVENTARIO_ID, ENCARGADO_FINANZAS_ID
) VALUES
(
    'Proyecto Alpha', 
    'Desarrollo de la nueva plataforma Alpha.', 
    'Cronograma Alpha', 
    150000.00, 
    75000.00, 
    'Activo', 
    'Alta', 
    '2024-01-15', 
    '2024-12-15', 
    1, 
    1, 
    1
),
(
    'Proyecto Beta', 
    'Implementación del sistema Beta en todas las sucursales.', 
    'Cronograma Beta', 
    200000.00, 
    100000.00, 
    'En Espera', 
    'Media', 
    '2024-02-01', 
    '2024-11-30', 
    2, 
    2, 
    2
);
