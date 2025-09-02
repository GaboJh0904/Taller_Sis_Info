-- ==============================================
-- Database: planificacion_inventario
-- ==============================================

CREATE SCHEMA IF NOT EXISTS planificacion_inventario;
USE planificacion_inventario;

-- =====================================================
-- 1. Insertar Empleados Adicionales
-- =====================================================

INSERT INTO EMPLEADO (NOMBRE, ROL, TELFONO, FECHA_REGISTRO) VALUES
('AnaMartinez', 'Operario', '555-2345', 20230201),
('LuisFernandez', 'Supervisor', '555-3456', 20230301),
('SofiaRamirez', 'Analista', '555-4567', 20230401),
('PedroSanchez', 'Operario', '555-5678', 20230501),
('LauraGarcia', 'Supervisor', '555-6789', 20230601),
('JorgeHernandez', 'Analista', '555-7890', 20230701),
('ElenaDiaz', 'Operario', '555-8901', 20230801),
('MiguelTorres', 'Supervisor', '555-9012', 20230901),
('IsabelLopez', 'Analista', '555-0123', 20231001),
('FernandoGutierrez', 'Operario', '555-1235', 20231101);

-- =====================================================
-- 2. Insertar Usuarios Correspondientes
-- =====================================================

INSERT INTO USUARIO (PASSWOR_HASH, USER_NAME, EMAIL, EMPLEADO_ID) VALUES
('$2a$12$1mHoKIOnfZ7LcEi6/8SgC.RD1ogm8MBeSfSk.3cbPve/8N21pVbmO', 'AnaMartinez', 'ana.martinez@example.com', 1),
('$2a$12$1mHoKIOnfZ7LcEi6/8SgC.RD1ogm8MBeSfSk.3cbPve/8N21pVbmO', 'LuisFernandez', 'luis.fernandez@example.com', 2),
('$2a$12$1mHoKIOnfZ7LcEi6/8SgC.RD1ogm8MBeSfSk.3cbPve/8N21pVbmO', 'SofiaRamirez', 'sofia.ramirez@example.com', 3),
('$2a$12$1mHoKIOnfZ7LcEi6/8SgC.RD1ogm8MBeSfSk.3cbPve/8N21pVbmO', 'PedroSanchez', 'pedro.sanchez@example.com', 4),
('$2a$12$1mHoKIOnfZ7LcEi6/8SgC.RD1ogm8MBeSfSk.3cbPve/8N21pVbmO', 'LauraGarcia', 'laura.garcia@example.com', 5),
('$2a$12$1mHoKIOnfZ7LcEi6/8SgC.RD1ogm8MBeSfSk.3cbPve/8N21pVbmO', 'JorgeHernandez', 'jorge.hernandez@example.com', 6),
('$2a$12$1mHoKIOnfZ7LcEi6/8SgC.RD1ogm8MBeSfSk.3cbPve/8N21pVbmO', 'ElenaDiaz', 'elena.diaz@example.com', 7),
('$2a$12$1mHoKIOnfZ7LcEi6/8SgC.RD1ogm8MBeSfSk.3cbPve/8N21pVbmO', 'MiguelTorres', 'miguel.torres@example.com', 8),
('$2a$12$1mHoKIOnfZ7LcEi6/8SgC.RD1ogm8MBeSfSk.3cbPve/8N21pVbmO', 'IsabelLopez', 'isabel.lopez@example.com', 9),
('$2a$12$1mHoKIOnfZ7LcEi6/8SgC.RD1ogm8MBeSfSk.3cbPve/8N21pVbmO', 'FernandoGutierrez', 'fernando.gutierrez@example.com', 10);

-- =====================================================
-- 3. Insertar Encargados de Almacén
-- =====================================================

INSERT INTO ENCARGADO_ALMACEN (NIVEL_ACCESO, NOTIFICACIONES_ACTIVAS, USUARIO_ID) VALUES
('Alto', TRUE, 1),
('Medio', FALSE, 2),
('Bajo', TRUE, 3),
('Alto', TRUE, 4),
('Medio', FALSE, 5),
('Bajo', TRUE, 6),
('Alto', TRUE, 7),
('Medio', FALSE, 8),
('Bajo', TRUE, 9),
('Alto', TRUE, 10);

-- =====================================================
-- 4. Insertar Encargados de Proyecto
-- =====================================================

INSERT INTO ENCARGADO_PROYECTO (USUARIO_ID) VALUES
(1),
(2),
(3),
(4),
(5),
(6),
(7),
(8),
(9),
(10);

-- =====================================================
-- 5. Insertar Encargados de Finanzas
-- =====================================================

INSERT INTO ENCARGADO_FINANZAS (USUARIO_ID) VALUES
(1),
(2),
(3),
(4),
(5),
(6),
(7),
(8),
(9),
(10);

-- =====================================================
-- 6. Insertar Gerentes de Inventario
-- =====================================================

INSERT INTO GERENTE_INVENTARIO (NIVEL_ACCESO, ENCARGADO_PEDIDOS, NOTIFICACIONES_ACTIVAS, USUARIO_ID) VALUES
('Alto', TRUE, TRUE, 1),
('Medio', FALSE, TRUE, 2),
('Bajo', TRUE, FALSE, 3),
('Alto', TRUE, TRUE, 4),
('Medio', FALSE, TRUE, 5),
('Bajo', TRUE, FALSE, 6),
('Alto', TRUE, TRUE, 7),
('Medio', FALSE, TRUE, 8),
('Bajo', TRUE, FALSE, 9),
('Alto', TRUE, TRUE, 10);

-- =====================================================
-- 7. Insertar Proveedores
-- =====================================================

INSERT INTO PROVEEDOR (NOMBRE, DIRECCION, TELEFONO) VALUES
('Proveedora ABC', 'Calle Falsa 123, Ciudad', '555-1111'),
('Materiales XYZ', 'Avenida Siempre Viva 456, Ciudad', '555-2222'),
('Herramientas LMN', 'Boulevard Central 789, Ciudad', '555-3333');

-- =====================================================
-- 8. Insertar Herramientas Adicionales
-- =====================================================

INSERT INTO HERRAMIENTA (NOMBRE, DESCRIPCION, CANTIDAD, PRECIO_UNITARIO, CANTIDAD_MINIMA) VALUES
('Taladro Eléctrico', 'Taladro con varias velocidades', 50, 150, 10),
('Martillo', 'Martillo de acero', 100, 20, 15),
('Sierra Circular', 'Sierra para cortar madera', 30, 200, 5),
('Nivel Láser', 'Nivel con proyección láser', 25, 300, 3),
('Compresor de Aire', 'Compresor portátil', 10, 500, 2),
('Atornillador Inalámbrico', 'Atornillador con batería recargable', 40, 80, 8),
('Cinta Métrica', 'Cinta métrica de 5 metros', 200, 10, 20),
('Escalera Extensible', 'Escalera de aluminio', 15, 120, 4),
('Pistola de Calor', 'Pistola para trabajo con plásticos', 20, 90, 5),
('Multiherramienta', 'Herramienta multifunción', 35, 60, 7),
('Guantes de Seguridad', 'Guantes resistentes a cortes', 500, 5, 100),
('Casco de Protección', 'Casco con visera', 300, 20, 50),
('Protector Auditivo', 'Tapones para oídos', 1000, 2, 200),
('Botas de Trabajo', 'Botas con punta de acero', 400, 30, 80),
('Chaqueta Reflectante', 'Chaqueta para alta visibilidad', 250, 15, 40);

-- =====================================================
-- 9. Insertar Materiales Adicionales
-- =====================================================

INSERT INTO MATERIAL (NOMBRE, DESCRIPCION, CANTIDAD, PRECIO_UNITARIO, CANTIDAD_MINIMA) VALUES
('Cemento', 'Cemento Portland 50kg', 1000, 8, 200),
('Arena', 'Arena fina para construcción', 5000, 3, 1000),
('Grava', 'Grava de 3/4 pulgadas', 3000, 4, 800),
('Varilla de Acero', 'Varilla de 12mm', 2000, 5, 500),
('Ladrillo', 'Ladrillo de arcilla', 10000, 1, 2000),
('Hormigón Premezclado', 'Hormigón listo para usar', 800, 100, 150),
('Madera de Pino', 'Tablas de pino 2x4', 4000, 7, 800),
('PVC', 'Tubos de PVC 2 pulgadas', 1500, 6, 300),
('Vidrio', 'Vidrio templado 6mm', 1200, 15, 250),
('Pintura Blanca', 'Pintura al agua', 500, 20, 100),
('Barras de Refuerzo', 'Barras de acero para refuerzo', 1500, 10, 300),
('Tornillos de Madera', 'Tornillos para madera 4x50mm', 8000, 0.3, 1600),
('Adhesivo Epoxi', 'Adhesivo de dos componentes', 500, 25, 100),
('Cables de Energía', 'Cables eléctricos 10mm', 3000, 7, 600),
('Tuberías de Acero', 'Tuberías de acero galvanizado', 1000, 20, 200),
('Bloque de Hormigón', 'Bloque de hormigón 20x20x40', 5000, 2, 1000),
('Pintura Azul', 'Pintura al agua color azul', 800, 18, 200),
('Cable Eléctrico', 'Cable eléctrico de 3 conductores', 2000, 5, 400),
('Tubo de PVC', 'Tubo de PVC de 4 pulgadas', 1500, 6, 300),
('Placa de Yeso', 'Placa de yeso 1.2x2.4 metros', 3000, 10, 600),
('Tornillos', 'Tornillos de acero 5x50mm', 10000, 0.5, 2000),
('Clavos', 'Clavos de 4 pulgadas', 20000, 0.1, 5000),
('Anclajes', 'Anclajes para concreto', 5000, 1.5, 1000),
('Masilla', 'Masilla para acabados', 1000, 4, 200),
('Cemento Rápido', 'Cemento de fraguado rápido', 800, 10, 160);

-- =====================================================
-- 10. Insertar Almacenes Adicionales
-- =====================================================

INSERT INTO ALMACEN (UBICACION, FECHA_ACTUALIZACION, ENCARGADO_ALMACEN_ID) VALUES
('Centro Logístico', '2024-01-10', 1),
('Sucursal Norte', '2024-02-15', 2),
('Sucursal Sur', '2024-03-20', 3),
('Depósito Este', '2024-04-25', 4),
('Depósito Oeste', '2024-05-30', 5),
('Centro de Distribución', '2024-06-05', 6),
('Almacén Principal', '2024-07-10', 7),
('Almacén Secundario', '2024-08-15', 8),
('Almacén Tercero', '2024-09-20', 9),
('Almacén Cuarto', '2024-10-25', 10);

-- =====================================================
-- 11. Insertar Proyectos Adicionales
-- =====================================================

INSERT INTO PROYECTO (
    NOMBRE, DESCRIPCION, CRONOGRAMA, PRESUPUESTO_ASIGNADO, METAS_FINANCIERAS, 
    ESTADO, PRIORIDAD, FECHA_INICIO, FECHA_FIN, 
    ENCARGADO_PROYECTO_ID, GERENTE_INVENTARIO_ID, ENCARGADO_FINANZAS_ID
) VALUES
(
    'Proyecto Gamma', 
    'Construcción del puente Gamma.', 
    'Cronograma Gamma', 
    300000.00, 
    150000.00, 
    'Activo', 
    'Alta', 
    '2024-01-05', 
    '2024-12-20', 
    1, 
    1, 
    1
),
(
    'Proyecto Delta', 
    'Renovación del edificio Delta.', 
    'Cronograma Delta', 
    250000.00, 
    125000.00, 
    'Activo', 
    'Alta', 
    '2024-02-01', 
    '2024-11-30', 
    2, 
    2, 
    2
),
(
    'Proyecto Epsilon', 
    'Construcción de la planta Epsilon.', 
    'Cronograma Epsilon', 
    400000.00, 
    200000.00, 
    'Activo', 
    'Alta', 
    '2024-03-01', 
    '2024-12-31', 
    3, 
    3, 
    3
),
(
    'Proyecto Zeta', 
    'Expansión de la infraestructura Zeta.', 
    'Cronograma Zeta', 
    350000.00, 
    175000.00, 
    'Activo', 
    'Alta', 
    '2024-04-01', 
    '2024-12-15', 
    4, 
    4, 
    4
);

-- =====================================================
-- 12. Insertar Flujos y Asignaciones de Herramientas y Materiales para Proyectos
-- =====================================================

-- Nota: Los IDs de FLUJO_HERRAMIENTA y FLUJO_MATERIAL se asumen que empiezan desde 1 y se incrementan automáticamente.

-- ==============================================
-- Proyecto Gamma (ID=1)
-- ==============================================

-- ------------------------------------------------
-- Flujos de Herramientas para Proyecto Gamma
-- ------------------------------------------------

-- Preparacion
INSERT INTO FLUJO_HERRAMIENTA (CANTIDAD, MOVIMIENTO, FECHA, ALMACEN_ID, HERRAMIENTA_ID) VALUES
(10, 'entrada', '2024-01-10', 1, 1),
(20, 'entrada', '2024-01-12', 1, 2),
(5, 'entrada', '2024-01-15', 1, 3),
(8, 'entrada', '2024-01-18', 1, 4);

-- Cimentacion
INSERT INTO FLUJO_HERRAMIENTA (CANTIDAD, MOVIMIENTO, FECHA, ALMACEN_ID, HERRAMIENTA_ID) VALUES
(7, 'salida', '2024-02-05', 2, 1),
(15, 'salida', '2024-02-07', 2, 2),
(3, 'salida', '2024-02-10', 2, 3),
(4, 'salida', '2024-02-12', 2, 4);

-- Obra Gruesa
INSERT INTO FLUJO_HERRAMIENTA (CANTIDAD, MOVIMIENTO, FECHA, ALMACEN_ID, HERRAMIENTA_ID) VALUES
(5, 'salida', '2024-03-15', 3, 1),
(10, 'salida', '2024-03-18', 3, 2),
(2, 'salida', '2024-03-20', 3, 3),
(3, 'salida', '2024-03-22', 3, 4);

-- Obra Fina
INSERT INTO FLUJO_HERRAMIENTA (CANTIDAD, MOVIMIENTO, FECHA, ALMACEN_ID, HERRAMIENTA_ID) VALUES
(4, 'salida', '2024-06-10', 4, 1),
(8, 'salida', '2024-06-12', 4, 2),
(1, 'salida', '2024-06-15', 4, 3),
(2, 'salida', '2024-06-18', 4, 4);

-- Inspeccion
INSERT INTO FLUJO_HERRAMIENTA (CANTIDAD, MOVIMIENTO, FECHA, ALMACEN_ID, HERRAMIENTA_ID) VALUES
(3, 'salida', '2024-09-05', 5, 1),
(6, 'salida', '2024-09-07', 5, 2),
(1, 'salida', '2024-09-10', 5, 3),
(2, 'salida', '2024-09-12', 5, 4);

-- ------------------------------------------------
-- Asignaciones de Herramientas para Proyecto Gamma
-- ------------------------------------------------

-- Preparacion
INSERT INTO ASIGNACION_HERRAMIENTA (CANTIDAD, FLUJO_HERRAMIENTA_ID, PROYECTO_ID, FASE) VALUES
(10, 1, 1, 'preparacion'),
(20, 2, 1, 'preparacion'),
(5, 3, 1, 'preparacion'),
(8, 4, 1, 'preparacion');

-- Cimentacion
INSERT INTO ASIGNACION_HERRAMIENTA (CANTIDAD, FLUJO_HERRAMIENTA_ID, PROYECTO_ID, FASE) VALUES
(7, 5, 1, 'cimentacion'),
(15, 6, 1, 'cimentacion'),
(3, 7, 1, 'cimentacion'),
(4, 8, 1, 'cimentacion');

-- Obra Gruesa
INSERT INTO ASIGNACION_HERRAMIENTA (CANTIDAD, FLUJO_HERRAMIENTA_ID, PROYECTO_ID, FASE) VALUES
(5, 9, 1, 'obra_gruesa'),
(10, 10, 1, 'obra_gruesa'),
(2, 11, 1, 'obra_gruesa'),
(3, 12, 1, 'obra_gruesa');

-- Obra Fina
INSERT INTO ASIGNACION_HERRAMIENTA (CANTIDAD, FLUJO_HERRAMIENTA_ID, PROYECTO_ID, FASE) VALUES
(4, 13, 1, 'obra_fina'),
(8, 14, 1, 'obra_fina'),
(1, 15, 1, 'obra_fina'),
(2, 16, 1, 'obra_fina');

-- Inspeccion
INSERT INTO ASIGNACION_HERRAMIENTA (CANTIDAD, FLUJO_HERRAMIENTA_ID, PROYECTO_ID, FASE) VALUES
(3, 17, 1, 'inspeccion'),
(6, 18, 1, 'inspeccion'),
(1, 19, 1, 'inspeccion'),
(2, 20, 1, 'inspeccion');

-- ------------------------------------------------
-- Flujos de Materiales para Proyecto Gamma
-- ------------------------------------------------

-- Preparacion
INSERT INTO FLUJO_MATERIAL (MATERIAL_ID, ALMACEN_ID, CANTIDAD, MOVIMIENTO, FECHA) VALUES
(1, 1, 500, 'entrada', '2024-01-11'),
(2, 1, 2000, 'entrada', '2024-01-13'),
(3, 1, 1500, 'entrada', '2024-01-16'),
(4, 1, 800, 'entrada', '2024-01-19');

-- Cimentacion
INSERT INTO FLUJO_MATERIAL (MATERIAL_ID, ALMACEN_ID, CANTIDAD, MOVIMIENTO, FECHA) VALUES
(1, 2, -200, 'salida', '2024-02-06'),
(2, 2, -500, 'salida', '2024-02-08'),
(3, 2, -300, 'salida', '2024-02-11'),
(4, 2, -100, 'salida', '2024-02-13');

-- Obra Gruesa
INSERT INTO FLUJO_MATERIAL (MATERIAL_ID, ALMACEN_ID, CANTIDAD, MOVIMIENTO, FECHA) VALUES
(1, 3, -100, 'salida', '2024-03-16'),
(2, 3, -300, 'salida', '2024-03-19'),
(3, 3, -200, 'salida', '2024-03-21'),
(4, 3, -150, 'salida', '2024-03-23');

-- Obra Fina
INSERT INTO FLUJO_MATERIAL (MATERIAL_ID, ALMACEN_ID, CANTIDAD, MOVIMIENTO, FECHA) VALUES
(1, 4, -150, 'salida', '2024-06-11'),
(2, 4, -400, 'salida', '2024-06-13'),
(3, 4, -250, 'salida', '2024-06-16'),
(4, 4, -200, 'salida', '2024-06-19');

-- Inspeccion
INSERT INTO FLUJO_MATERIAL (MATERIAL_ID, ALMACEN_ID, CANTIDAD, MOVIMIENTO, FECHA) VALUES
(1, 5, -50, 'salida', '2024-09-06'),
(2, 5, -100, 'salida', '2024-09-08'),
(3, 5, -80, 'salida', '2024-09-11'),
(4, 5, -70, 'salida', '2024-09-13');

-- ------------------------------------------------
-- Asignaciones de Materiales para Proyecto Gamma
-- ------------------------------------------------

-- Preparacion
INSERT INTO ASIGNACION_MATERIAL (FLUJO_MATERIAL_ID, PROYECTO_ID, CANTIDAD, FASE) VALUES
(1, 1, 500, 'preparacion'),
(2, 1, 2000, 'preparacion'),
(3, 1, 1500, 'preparacion'),
(4, 1, 800, 'preparacion');

-- Cimentacion
INSERT INTO ASIGNACION_MATERIAL (FLUJO_MATERIAL_ID, PROYECTO_ID, CANTIDAD, FASE) VALUES
(5, 1, 200, 'cimentacion'),
(6, 1, 500, 'cimentacion'),
(7, 1, 300, 'cimentacion'),
(8, 1, 100, 'cimentacion');

-- Obra Gruesa
INSERT INTO ASIGNACION_MATERIAL (FLUJO_MATERIAL_ID, PROYECTO_ID, CANTIDAD, FASE) VALUES
(9, 1, 100, 'obra_gruesa'),
(10, 1, 300, 'obra_gruesa'),
(11, 1, 200, 'obra_gruesa'),
(12, 1, 150, 'obra_gruesa');

-- Obra Fina
INSERT INTO ASIGNACION_MATERIAL (FLUJO_MATERIAL_ID, PROYECTO_ID, CANTIDAD, FASE) VALUES
(13, 1, 150, 'obra_fina'),
(14, 1, 400, 'obra_fina'),
(15, 1, 250, 'obra_fina'),
(16, 1, 200, 'obra_fina');

-- Inspeccion
INSERT INTO ASIGNACION_MATERIAL (FLUJO_MATERIAL_ID, PROYECTO_ID, CANTIDAD, FASE) VALUES
(17, 1, 50, 'inspeccion'),
(18, 1, 100, 'inspeccion'),
(19, 1, 80, 'inspeccion'),
(20, 1, 70, 'inspeccion');

-- ==============================================
-- Proyecto Delta (ID=2)
-- ==============================================

-- ------------------------------------------------
-- Flujos de Herramientas para Proyecto Delta
-- ------------------------------------------------

-- Preparacion
INSERT INTO FLUJO_HERRAMIENTA (CANTIDAD, MOVIMIENTO, FECHA, ALMACEN_ID, HERRAMIENTA_ID) VALUES
(5, 'entrada', '2024-02-05', 2, 1),
(10, 'entrada', '2024-02-07', 2, 2),
(2, 'entrada', '2024-02-10', 2, 3),
(3, 'entrada', '2024-02-12', 2, 4);

-- Cimentacion
INSERT INTO FLUJO_HERRAMIENTA (CANTIDAD, MOVIMIENTO, FECHA, ALMACEN_ID, HERRAMIENTA_ID) VALUES
(7, 'salida', '2024-03-05', 3, 1),
(15, 'salida', '2024-03-07', 3, 2),
(3, 'salida', '2024-03-10', 3, 3),
(4, 'salida', '2024-03-12', 3, 4);

-- Obra Gruesa
INSERT INTO FLUJO_HERRAMIENTA (CANTIDAD, MOVIMIENTO, FECHA, ALMACEN_ID, HERRAMIENTA_ID) VALUES
(5, 'salida', '2024-04-15', 4, 1),
(10, 'salida', '2024-04-18', 4, 2),
(2, 'salida', '2024-04-20', 4, 3),
(3, 'salida', '2024-04-22', 4, 4);

-- Obra Fina
INSERT INTO FLUJO_HERRAMIENTA (CANTIDAD, MOVIMIENTO, FECHA, ALMACEN_ID, HERRAMIENTA_ID) VALUES
(4, 'salida', '2024-07-10', 5, 1),
(8, 'salida', '2024-07-12', 5, 2),
(1, 'salida', '2024-07-15', 5, 3),
(2, 'salida', '2024-07-18', 5, 4);

-- Inspeccion
INSERT INTO FLUJO_HERRAMIENTA (CANTIDAD, MOVIMIENTO, FECHA, ALMACEN_ID, HERRAMIENTA_ID) VALUES
(3, 'salida', '2024-10-05', 6, 1),
(6, 'salida', '2024-10-07', 6, 2),
(1, 'salida', '2024-10-10', 6, 3),
(2, 'salida', '2024-10-12', 6, 4);

-- ------------------------------------------------
-- Asignaciones de Herramientas para Proyecto Delta
-- ------------------------------------------------

-- Preparacion
INSERT INTO ASIGNACION_HERRAMIENTA (CANTIDAD, FLUJO_HERRAMIENTA_ID, PROYECTO_ID, FASE) VALUES
(5, 21, 2, 'preparacion'),
(10, 22, 2, 'preparacion'),
(2, 23, 2, 'preparacion'),
(3, 24, 2, 'preparacion');

-- Cimentacion
INSERT INTO ASIGNACION_HERRAMIENTA (CANTIDAD, FLUJO_HERRAMIENTA_ID, PROYECTO_ID, FASE) VALUES
(7, 25, 2, 'cimentacion'),
(15, 26, 2, 'cimentacion'),
(3, 27, 2, 'cimentacion'),
(4, 28, 2, 'cimentacion');

-- Obra Gruesa
INSERT INTO ASIGNACION_HERRAMIENTA (CANTIDAD, FLUJO_HERRAMIENTA_ID, PROYECTO_ID, FASE) VALUES
(5, 29, 2, 'obra_gruesa'),
(10, 30, 2, 'obra_gruesa'),
(2, 31, 2, 'obra_gruesa'),
(3, 32, 2, 'obra_gruesa');

-- Obra Fina
INSERT INTO ASIGNACION_HERRAMIENTA (CANTIDAD, FLUJO_HERRAMIENTA_ID, PROYECTO_ID, FASE) VALUES
(4, 33, 2, 'obra_fina'),
(8, 34, 2, 'obra_fina'),
(1, 35, 2, 'obra_fina'),
(2, 36, 2, 'obra_fina');

-- Inspeccion
INSERT INTO ASIGNACION_HERRAMIENTA (CANTIDAD, FLUJO_HERRAMIENTA_ID, PROYECTO_ID, FASE) VALUES
(3, 37, 2, 'inspeccion'),
(6, 38, 2, 'inspeccion'),
(1, 39, 2, 'inspeccion'),
(2, 40, 2, 'inspeccion');

-- ------------------------------------------------
-- Flujos de Materiales para Proyecto Delta
-- ------------------------------------------------

-- Preparacion
INSERT INTO FLUJO_MATERIAL (MATERIAL_ID, ALMACEN_ID, CANTIDAD, MOVIMIENTO, FECHA) VALUES
(6, 2, 600, 'entrada', '2024-02-06'),
(7, 2, 2500, 'entrada', '2024-02-08'),
(8, 2, 1800, 'entrada', '2024-02-11'),
(9, 2, 1000, 'entrada', '2024-02-14');

-- Cimentacion
INSERT INTO FLUJO_MATERIAL (MATERIAL_ID, ALMACEN_ID, CANTIDAD, MOVIMIENTO, FECHA) VALUES
(6, 3, -300, 'salida', '2024-03-06'),
(7, 3, -700, 'salida', '2024-03-08'),
(8, 3, -400, 'salida', '2024-03-11'),
(9, 3, -200, 'salida', '2024-03-14');

-- Obra Gruesa
INSERT INTO FLUJO_MATERIAL (MATERIAL_ID, ALMACEN_ID, CANTIDAD, MOVIMIENTO, FECHA) VALUES
(6, 4, -150, 'salida', '2024-04-16'),
(7, 4, -500, 'salida', '2024-04-18'),
(8, 4, -350, 'salida', '2024-04-21'),
(9, 4, -250, 'salida', '2024-04-23');

-- Obra Fina
INSERT INTO FLUJO_MATERIAL (MATERIAL_ID, ALMACEN_ID, CANTIDAD, MOVIMIENTO, FECHA) VALUES
(6, 5, -200, 'salida', '2024-07-11'),
(7, 5, -600, 'salida', '2024-07-13'),
(8, 5, -450, 'salida', '2024-07-16'),
(9, 5, -300, 'salida', '2024-07-19');

-- Inspeccion
INSERT INTO FLUJO_MATERIAL (MATERIAL_ID, ALMACEN_ID, CANTIDAD, MOVIMIENTO, FECHA) VALUES
(6, 6, -50, 'salida', '2024-10-06'),
(7, 6, -100, 'salida', '2024-10-08'),
(8, 6, -80, 'salida', '2024-10-11'),
(9, 6, -70, 'salida', '2024-10-14');

-- ------------------------------------------------
-- Asignaciones de Materiales para Proyecto Delta
-- ------------------------------------------------

-- Preparacion
INSERT INTO ASIGNACION_MATERIAL (FLUJO_MATERIAL_ID, PROYECTO_ID, CANTIDAD, FASE) VALUES
(21, 2, 600, 'preparacion'),
(22, 2, 2500, 'preparacion'),
(23, 2, 1800, 'preparacion'),
(24, 2, 1000, 'preparacion');

-- Cimentacion
INSERT INTO ASIGNACION_MATERIAL (FLUJO_MATERIAL_ID, PROYECTO_ID, CANTIDAD, FASE) VALUES
(25, 2, 300, 'cimentacion'),
(26, 2, 700, 'cimentacion'),
(27, 2, 400, 'cimentacion'),
(28, 2, 200, 'cimentacion');

-- Obra Gruesa
INSERT INTO ASIGNACION_MATERIAL (FLUJO_MATERIAL_ID, PROYECTO_ID, CANTIDAD, FASE) VALUES
(29, 2, 150, 'obra_gruesa'),
(30, 2, 500, 'obra_gruesa'),
(31, 2, 350, 'obra_gruesa'),
(32, 2, 250, 'obra_gruesa');

-- Obra Fina
INSERT INTO ASIGNACION_MATERIAL (FLUJO_MATERIAL_ID, PROYECTO_ID, CANTIDAD, FASE) VALUES
(33, 2, 200, 'obra_fina'),
(34, 2, 600, 'obra_fina'),
(35, 2, 450, 'obra_fina'),
(36, 2, 300, 'obra_fina');

-- Inspeccion
INSERT INTO ASIGNACION_MATERIAL (FLUJO_MATERIAL_ID, PROYECTO_ID, CANTIDAD, FASE) VALUES
(37, 2, 50, 'inspeccion'),
(38, 2, 100, 'inspeccion'),
(39, 2, 80, 'inspeccion'),
(40, 2, 70, 'inspeccion');

-- ==============================================
-- Proyecto Epsilon (ID=3)
-- ==============================================

-- ------------------------------------------------
-- Flujos de Herramientas para Proyecto Epsilon
-- ------------------------------------------------

-- Preparacion
INSERT INTO FLUJO_HERRAMIENTA (CANTIDAD, MOVIMIENTO, FECHA, ALMACEN_ID, HERRAMIENTA_ID) VALUES
(6, 'entrada', '2024-03-05', 3, 1),
(12, 'entrada', '2024-03-07', 3, 2),
(3, 'entrada', '2024-03-10', 3, 3),
(5, 'entrada', '2024-03-12', 3, 4);

-- Cimentacion
INSERT INTO FLUJO_HERRAMIENTA (CANTIDAD, MOVIMIENTO, FECHA, ALMACEN_ID, HERRAMIENTA_ID) VALUES
(8, 'salida', '2024-04-05', 4, 1),
(20, 'salida', '2024-04-07', 4, 2),
(4, 'salida', '2024-04-10', 4, 3),
(6, 'salida', '2024-04-12', 4, 4);

-- Obra Gruesa
INSERT INTO FLUJO_HERRAMIENTA (CANTIDAD, MOVIMIENTO, FECHA, ALMACEN_ID, HERRAMIENTA_ID) VALUES
(7, 'salida', '2024-05-15', 5, 1),
(14, 'salida', '2024-05-18', 5, 2),
(5, 'salida', '2024-05-20', 5, 3),
(7, 'salida', '2024-05-22', 5, 4);

-- Obra Fina
INSERT INTO FLUJO_HERRAMIENTA (CANTIDAD, MOVIMIENTO, FECHA, ALMACEN_ID, HERRAMIENTA_ID) VALUES
(5, 'salida', '2024-08-10', 6, 1),
(10, 'salida', '2024-08-12', 6, 2),
(2, 'salida', '2024-08-15', 6, 3),
(3, 'salida', '2024-08-18', 6, 4);

-- Inspeccion
INSERT INTO FLUJO_HERRAMIENTA (CANTIDAD, MOVIMIENTO, FECHA, ALMACEN_ID, HERRAMIENTA_ID) VALUES
(4, 'salida', '2024-11-05', 7, 1),
(9, 'salida', '2024-11-07', 7, 2),
(1, 'salida', '2024-11-10', 7, 3),
(2, 'salida', '2024-11-12', 7, 4);

-- ------------------------------------------------
-- Asignaciones de Herramientas para Proyecto Epsilon
-- ------------------------------------------------

-- Preparacion
INSERT INTO ASIGNACION_HERRAMIENTA (CANTIDAD, FLUJO_HERRAMIENTA_ID, PROYECTO_ID, FASE) VALUES
(6, 41, 3, 'preparacion'),
(12, 42, 3, 'preparacion'),
(3, 43, 3, 'preparacion'),
(5, 44, 3, 'preparacion');

-- Cimentacion
INSERT INTO ASIGNACION_HERRAMIENTA (CANTIDAD, FLUJO_HERRAMIENTA_ID, PROYECTO_ID, FASE) VALUES
(8, 45, 3, 'cimentacion'),
(20, 46, 3, 'cimentacion'),
(4, 47, 3, 'cimentacion'),
(6, 48, 3, 'cimentacion');

-- Obra Gruesa
INSERT INTO ASIGNACION_HERRAMIENTA (CANTIDAD, FLUJO_HERRAMIENTA_ID, PROYECTO_ID, FASE) VALUES
(7, 49, 3, 'obra_gruesa'),
(14, 50, 3, 'obra_gruesa'),
(5, 51, 3, 'obra_gruesa'),
(7, 52, 3, 'obra_gruesa');

-- Obra Fina
INSERT INTO ASIGNACION_HERRAMIENTA (CANTIDAD, FLUJO_HERRAMIENTA_ID, PROYECTO_ID, FASE) VALUES
(5, 53, 3, 'obra_fina'),
(10, 54, 3, 'obra_fina'),
(2, 55, 3, 'obra_fina'),
(3, 56, 3, 'obra_fina');

-- Inspeccion
INSERT INTO ASIGNACION_HERRAMIENTA (CANTIDAD, FLUJO_HERRAMIENTA_ID, PROYECTO_ID, FASE) VALUES
(4, 57, 3, 'inspeccion'),
(9, 58, 3, 'inspeccion'),
(1, 59, 3, 'inspeccion'),
(2, 60, 3, 'inspeccion');

-- ------------------------------------------------
-- Flujos de Materiales para Proyecto Epsilon
-- ------------------------------------------------

-- Preparacion
INSERT INTO FLUJO_MATERIAL (MATERIAL_ID, ALMACEN_ID, CANTIDAD, MOVIMIENTO, FECHA) VALUES
(6, 3, 700, 'entrada', '2024-03-06'),
(7, 3, 3000, 'entrada', '2024-03-08'),
(8, 3, 2000, 'entrada', '2024-03-11'),
(9, 3, 1200, 'entrada', '2024-03-14');

-- Cimentacion
INSERT INTO FLUJO_MATERIAL (MATERIAL_ID, ALMACEN_ID, CANTIDAD, MOVIMIENTO, FECHA) VALUES
(6, 4, -400, 'salida', '2024-04-06'),
(7, 4, -800, 'salida', '2024-04-08'),
(8, 4, -600, 'salida', '2024-04-11'),
(9, 4, -500, 'salida', '2024-04-14');

-- Obra Gruesa
INSERT INTO FLUJO_MATERIAL (MATERIAL_ID, ALMACEN_ID, CANTIDAD, MOVIMIENTO, FECHA) VALUES
(6, 5, -200, 'salida', '2024-05-16'),
(7, 5, -1000, 'salida', '2024-05-18'),
(8, 5, -700, 'salida', '2024-05-21'),
(9, 5, -400, 'salida', '2024-05-23');

-- Obra Fina
INSERT INTO FLUJO_MATERIAL (MATERIAL_ID, ALMACEN_ID, CANTIDAD, MOVIMIENTO, FECHA) VALUES
(6, 6, -300, 'salida', '2024-08-11'),
(7, 6, -900, 'salida', '2024-08-13'),
(8, 6, -600, 'salida', '2024-08-16'),
(9, 6, -400, 'salida', '2024-08-19');

-- Inspeccion
INSERT INTO FLUJO_MATERIAL (MATERIAL_ID, ALMACEN_ID, CANTIDAD, MOVIMIENTO, FECHA) VALUES
(6, 7, -50, 'salida', '2024-10-06'),
(7, 7, -100, 'salida', '2024-10-08'),
(8, 7, -80, 'salida', '2024-10-11'),
(9, 7, -70, 'salida', '2024-10-14');

-- ------------------------------------------------
-- Asignaciones de Materiales para Proyecto Epsilon
-- ------------------------------------------------

-- Preparacion
INSERT INTO ASIGNACION_MATERIAL (FLUJO_MATERIAL_ID, PROYECTO_ID, CANTIDAD, FASE) VALUES
(21, 3, 700, 'preparacion'),
(22, 3, 3000, 'preparacion'),
(23, 3, 2000, 'preparacion'),
(24, 3, 1200, 'preparacion');

-- Cimentacion
INSERT INTO ASIGNACION_MATERIAL (FLUJO_MATERIAL_ID, PROYECTO_ID, CANTIDAD, FASE) VALUES
(25, 3, 400, 'cimentacion'),
(26, 3, 800, 'cimentacion'),
(27, 3, 600, 'cimentacion'),
(28, 3, 500, 'cimentacion');

-- Obra Gruesa
INSERT INTO ASIGNACION_MATERIAL (FLUJO_MATERIAL_ID, PROYECTO_ID, CANTIDAD, FASE) VALUES
(29, 3, 200, 'obra_gruesa'),
(30, 3, 1000, 'obra_gruesa'),
(31, 3, 700, 'obra_gruesa'),
(32, 3, 400, 'obra_gruesa');

-- Obra Fina
INSERT INTO ASIGNACION_MATERIAL (FLUJO_MATERIAL_ID, PROYECTO_ID, CANTIDAD, FASE) VALUES
(33, 3, 300, 'obra_fina'),
(34, 3, 900, 'obra_fina'),
(35, 3, 600, 'obra_fina'),
(36, 3, 400, 'obra_fina');

-- Inspeccion
INSERT INTO ASIGNACION_MATERIAL (FLUJO_MATERIAL_ID, PROYECTO_ID, CANTIDAD, FASE) VALUES
(37, 3, 50, 'inspeccion'),
(38, 3, 100, 'inspeccion'),
(39, 3, 80, 'inspeccion'),
(40, 3, 70, 'inspeccion');

-- ==============================================
-- Proyecto Zeta (ID=4)
-- ==============================================

-- ------------------------------------------------
-- Flujos de Herramientas para Proyecto Zeta
-- ------------------------------------------------

-- Preparacion
INSERT INTO FLUJO_HERRAMIENTA (CANTIDAD, MOVIMIENTO, FECHA, ALMACEN_ID, HERRAMIENTA_ID) VALUES
(7, 'entrada', '2024-05-05', 7, 1),
(14, 'entrada', '2024-05-07', 7, 2),
(3, 'entrada', '2024-05-10', 7, 3),
(5, 'entrada', '2024-05-12', 7, 4);

-- Cimentacion
INSERT INTO FLUJO_HERRAMIENTA (CANTIDAD, MOVIMIENTO, FECHA, ALMACEN_ID, HERRAMIENTA_ID) VALUES
(12, 'salida', '2024-07-05', 8, 1),
(30, 'salida', '2024-07-07', 8, 2),
(6, 'salida', '2024-07-10', 8, 3),
(8, 'salida', '2024-07-12', 8, 4);

-- Obra Gruesa
INSERT INTO FLUJO_HERRAMIENTA (CANTIDAD, MOVIMIENTO, FECHA, ALMACEN_ID, HERRAMIENTA_ID) VALUES
(10, 'salida', '2024-08-15', 9, 1),
(24, 'salida', '2024-08-18', 9, 2),
(5, 'salida', '2024-08-20', 9, 3),
(7, 'salida', '2024-08-22', 9, 4);

-- Obra Fina
INSERT INTO FLUJO_HERRAMIENTA (CANTIDAD, MOVIMIENTO, FECHA, ALMACEN_ID, HERRAMIENTA_ID) VALUES
(8, 'salida', '2024-10-10', 10, 1),
(16, 'salida', '2024-10-12', 10, 2),
(3, 'salida', '2024-10-15', 10, 3),
(4, 'salida', '2024-10-18', 10, 4);

-- Inspeccion
INSERT INTO FLUJO_HERRAMIENTA (CANTIDAD, MOVIMIENTO, FECHA, ALMACEN_ID, HERRAMIENTA_ID) VALUES
(6, 'salida', '2024-12-05', 1, 1),
(12, 'salida', '2024-12-07', 1, 2),
(2, 'salida', '2024-12-10', 1, 3),
(3, 'salida', '2024-12-12', 1, 4);

-- ------------------------------------------------
-- Asignaciones de Herramientas para Proyecto Zeta
-- ------------------------------------------------

-- Preparacion
INSERT INTO ASIGNACION_HERRAMIENTA (CANTIDAD, FLUJO_HERRAMIENTA_ID, PROYECTO_ID, FASE) VALUES
(7, 61, 4, 'preparacion'),
(14, 62, 4, 'preparacion'),
(3, 63, 4, 'preparacion'),
(5, 64, 4, 'preparacion');

-- Cimentacion
INSERT INTO ASIGNACION_HERRAMIENTA (CANTIDAD, FLUJO_HERRAMIENTA_ID, PROYECTO_ID, FASE) VALUES
(12, 65, 4, 'cimentacion'),
(30, 66, 4, 'cimentacion'),
(6, 67, 4, 'cimentacion'),
(8, 68, 4, 'cimentacion');

-- Obra Gruesa
INSERT INTO ASIGNACION_HERRAMIENTA (CANTIDAD, FLUJO_HERRAMIENTA_ID, PROYECTO_ID, FASE) VALUES
(10, 69, 4, 'obra_gruesa'),
(24, 70, 4, 'obra_gruesa'),
(5, 71, 4, 'obra_gruesa'),
(7, 72, 4, 'obra_gruesa');

-- Obra Fina
INSERT INTO ASIGNACION_HERRAMIENTA (CANTIDAD, FLUJO_HERRAMIENTA_ID, PROYECTO_ID, FASE) VALUES
(8, 73, 4, 'obra_fina'),
(16, 74, 4, 'obra_fina'),
(3, 75, 4, 'obra_fina'),
(4, 76, 4, 'obra_fina');

-- Inspeccion
INSERT INTO ASIGNACION_HERRAMIENTA (CANTIDAD, FLUJO_HERRAMIENTA_ID, PROYECTO_ID, FASE) VALUES
(6, 77, 4, 'inspeccion'),
(12, 78, 4, 'inspeccion'),
(2, 79, 4, 'inspeccion'),
(3, 80, 4, 'inspeccion');

-- ------------------------------------------------
-- Flujos de Materiales para Proyecto Zeta
-- ------------------------------------------------

-- Preparacion
INSERT INTO FLUJO_MATERIAL (MATERIAL_ID, ALMACEN_ID, CANTIDAD, MOVIMIENTO, FECHA) VALUES
(6, 7, -1000, 'salida', '2024-05-06'),
(7, 7, -4000, 'salida', '2024-05-08'),
(8, 7, -3000, 'salida', '2024-05-11'),
(9, 7, -2000, 'salida', '2024-05-14');

-- Cimentacion
INSERT INTO FLUJO_MATERIAL (MATERIAL_ID, ALMACEN_ID, CANTIDAD, MOVIMIENTO, FECHA) VALUES
(6, 8, -1200, 'salida', '2024-06-06'),
(7, 8, -1600, 'salida', '2024-06-08'),
(8, 8, -1000, 'salida', '2024-06-11'),
(9, 8, -600, 'salida', '2024-06-14');

-- Obra Gruesa
INSERT INTO FLUJO_MATERIAL (MATERIAL_ID, ALMACEN_ID, CANTIDAD, MOVIMIENTO, FECHA) VALUES
(6, 9, -1400, 'salida', '2024-07-16'),
(7, 9, -2400, 'salida', '2024-07-18'),
(8, 9, -1800, 'salida', '2024-07-21'),
(9, 9, -1200, 'salida', '2024-07-23');

-- Obra Fina
INSERT INTO FLUJO_MATERIAL (MATERIAL_ID, ALMACEN_ID, CANTIDAD, MOVIMIENTO, FECHA) VALUES
(6, 10, -1600, 'salida', '2024-08-11'),
(7, 10, -2800, 'salida', '2024-08-13'),
(8, 10, -2200, 'salida', '2024-08-16'),
(9, 10, -1500, 'salida', '2024-08-19');

-- Inspeccion
INSERT INTO FLUJO_MATERIAL (MATERIAL_ID, ALMACEN_ID, CANTIDAD, MOVIMIENTO, FECHA) VALUES
(6, 1, -2000, 'salida', '2024-11-06'),
(7, 1, -5000, 'salida', '2024-11-08'),
(8, 1, -3500, 'salida', '2024-11-11'),
(9, 1, -2500, 'salida', '2024-11-14');

-- ------------------------------------------------
-- Asignaciones de Materiales para Proyecto Zeta
-- ------------------------------------------------

-- Preparacion
INSERT INTO ASIGNACION_MATERIAL (FLUJO_MATERIAL_ID, PROYECTO_ID, CANTIDAD, FASE) VALUES
(101, 4, 1000, 'preparacion'),
(102, 4, 4000, 'preparacion'),
(103, 4, 3000, 'preparacion'),
(104, 4, 2000, 'preparacion');

-- Cimentacion
INSERT INTO ASIGNACION_MATERIAL (FLUJO_MATERIAL_ID, PROYECTO_ID, CANTIDAD, FASE) VALUES
(105, 4, 1200, 'cimentacion'),
(106, 4, 1600, 'cimentacion'),
(107, 4, 1000, 'cimentacion'),
(108, 4, 600, 'cimentacion');

-- Obra Gruesa
INSERT INTO ASIGNACION_MATERIAL (FLUJO_MATERIAL_ID, PROYECTO_ID, CANTIDAD, FASE) VALUES
(109, 4, 1400, 'obra_gruesa'),
(110, 4, 2400, 'obra_gruesa'),
(111, 4, 1800, 'obra_gruesa'),
(112, 4, 1200, 'obra_gruesa');

-- Obra Fina
INSERT INTO ASIGNACION_MATERIAL (FLUJO_MATERIAL_ID, PROYECTO_ID, CANTIDAD, FASE) VALUES
(113, 4, 1600, 'obra_fina'),
(114, 4, 2800, 'obra_fina'),
(115, 4, 2200, 'obra_fina'),
(116, 4, 1500, 'obra_fina');

-- Inspeccion
INSERT INTO ASIGNACION_MATERIAL (FLUJO_MATERIAL_ID, PROYECTO_ID, CANTIDAD, FASE) VALUES
(117, 4, 2000, 'inspeccion'),
(118, 4, 5000, 'inspeccion'),
(119, 4, 3500, 'inspeccion'),
(120, 4, 2500, 'inspeccion');

-- ==============================================
-- 13. Insertar Compras de Herramientas
-- ==============================================

INSERT INTO COMPRA_HERRAMIENTA (COSTO_TOTAL, PROVEEDOR_ID, FECHA, DETALLE) VALUES
(1500.00, 1, '2024-01-05 10:00:00', 'Compra inicial de herramientas para Proyecto Gamma.'),
(800.00, 2, '2024-03-10 14:30:00', 'Reposición de martillos y sierras.'),
(1200.00, 3, '2024-06-15 09:15:00', 'Adquisición de niveles láser y pistolas de calor.'),
(900.00, 1, '2024-09-20 16:45:00', 'Compra de compresores de aire y atornilladores.'),
(500.00, 2, '2024-11-25 11:00:00', 'Compra de cintas métricas y multiherramientas.'),
(2500.00, 1, '2024-04-05 09:00:00', 'Compra de guantes y cascos para Proyecto Epsilon.'),
(1800.00, 2, '2024-07-10 10:30:00', 'Compra de botas y chaquetas reflectantes.'),
(1500.00, 3, '2024-10-20 14:45:00', 'Compra de protectores auditivos y guantes adicionales.');

-- =====================================================
-- 14. Insertar Detalles de Compras de Herramientas
-- =====================================================

INSERT INTO DETALLE_COMPRA_HERRAMIENTA (COSTO, HERRAMIENTA_ID, COMPRA_HERRAMIENTA_ID, CANTIDAD) VALUES
(150.00, 1, 1, 10),
(20.00, 2, 1, 20),
(200.00, 3, 1, 5),
(300.00, 4, 1, 8),
(20.00, 2, 2, 40),
(200.00, 3, 2, 4),
(300.00, 4, 2, 6),
(500.00, 11, 3, 100),
(20.00, 12, 3, 150),
(2.00, 13, 3, 1000),
(30.00, 14, 4, 60),
(15.00, 15, 4, 250),
(5.00, 11, 5, 400),
(20.00, 12, 5, 100),
(2.00, 13, 5, 500),
(15.00, 15, 6, 250),
(5.00, 11, 6, 500),
(20.00, 12, 6, 200),
(2.00, 13, 6, 1000),
(15.00, 15, 7, 250),
(5.00, 11, 7, 500),
(20.00, 12, 7, 200),
(2.00, 13, 7, 1000),
(15.00, 15, 8, 250),
(5.00, 11, 8, 500),
(20.00, 12, 8, 200),
(2.00, 13, 8, 1000),
(15.00, 15, 9, 250),
(5.00, 11, 9, 500),
(20.00, 12, 9, 200),
(2.00, 13, 9, 1000),
(15.00, 15, 10, 250),
(5.00, 11, 10, 500),
(20.00, 12, 10, 200),
(2.00, 13, 10, 1000),
(15.00, 15, 11, 250),
(5.00, 11, 11, 500),
(20.00, 12, 11, 200),
(2.00, 13, 11, 1000),
(15.00, 15, 12, 250),
(5.00, 11, 12, 500),
(20.00, 12, 12, 200),
(2.00, 13, 12, 1000),
(15.00, 15, 13, 250),
(5.00, 11, 13, 500),
(20.00, 12, 13, 200),
(2.00, 13, 13, 1000),
(15.00, 15, 14, 250),
(5.00, 11, 14, 500),
(20.00, 12, 14, 200),
(2.00, 13, 14, 1000),
(15.00, 15, 15, 250),
(5.00, 11, 15, 500),
(20.00, 12, 15, 200),
(2.00, 13, 15, 1000),
(15.00, 15, 16, 250),
(5.00, 11, 16, 500),
(20.00, 12, 16, 200),
(2.00, 13, 16, 1000),
(15.00, 15, 17, 250),
(5.00, 11, 17, 500),
(20.00, 12, 17, 200),
(2.00, 13, 17, 1000),
(15.00, 15, 18, 250),
(5.00, 11, 18, 500),
(20.00, 12, 18, 200),
(2.00, 13, 18, 1000),
(15.00, 15, 19, 250),
(5.00, 11, 19, 500),
(20.00, 12, 19, 200),
(2.00, 13, 19, 1000),
(15.00, 15, 20, 250),
(5.00, 11, 20, 500),
(20.00, 12, 20, 200),
(2.00, 13, 20, 1000);

-- =====================================================
-- 15. Insertar Compras de Materiales
-- =====================================================

INSERT INTO COMPRA_MATERIAL (COSTO_TOTAL, FECHA, PROVEEDOR_ID, DETALLE) VALUES
(4000.00, '2024-01-08 08:00:00', 1, 'Compra inicial de materiales para Proyecto Gamma.'),
(1500.00, '2024-03-15 13:20:00', 2, 'Reposición de cemento y arena.'),
(2500.00, '2024-06-20 10:10:00', 3, 'Adquisición de varillas y ladrillos.'),
(1800.00, '2024-09-25 15:50:00', 1, 'Compra de hormigón premezclado y PVC.'),
(1200.00, '2024-11-30 12:30:00', 2, 'Compra de vidrio y pintura blanca.'),
(5000.00, '2024-02-10 10:00:00', 1, 'Compra de barras de refuerzo y tornillos.'),
(3000.00, '2024-05-15 11:30:00', 2, 'Compra de adhesivos y cables de energía.'),
(4000.00, '2024-08-20 09:45:00', 3, 'Compra de tuberías de acero y tornillos de madera.');

-- =====================================================
-- 16. Insertar Detalles de Compras de Materiales
-- =====================================================

INSERT INTO DETALLE_COMPRA_MATERIAL (COSTO, CANTIDAD, MATERIAL_ID, COMPRA_MATERIAL_ID) VALUES
(8.00, 500, 1, 1),
(3.00, 2000, 2, 1),
(4.00, 1500, 3, 1),
(5.00, 800, 4, 1),
(8.00, 300, 1, 2),
(3.00, 1200, 2, 2),
(4.00, 900, 3, 2),
(5.00, 400, 4, 2),
(1.00, 1000, 5, 3),
(8.00, 100, 1, 3),
(3.00, 400, 2, 3),
(4.00, 300, 3, 3),
(5.00, 200, 4, 3),
(1.00, 2000, 5, 4),
(20.00, 100, 10, 4),
(15.00, 80, 9, 4),
(20.00, 50, 10, 4),
(10.00, 1500, 6, 5),
(0.30, 8000, 7, 5),
(25.00, 200, 8, 5),
(7.00, 3000, 9, 5),
(20.00, 1000, 10, 5),
(10.00, 1500, 6, 6),
(0.30, 8000, 7, 6),
(25.00, 200, 8, 6),
(7.00, 3000, 9, 6),
(20.00, 1000, 10, 6),
(10.00, 1500, 6, 7),
(0.30, 8000, 7, 7),
(25.00, 200, 8, 7),
(7.00, 3000, 9, 7),
(20.00, 1000, 10, 7),
(10.00, 1500, 6, 8),
(0.30, 8000, 7, 8),
(25.00, 200, 8, 8),
(7.00, 3000, 9, 8),
(20.00, 1000, 10, 8),
(10.00, 1500, 6, 9),
(0.30, 8000, 7, 9),
(25.00, 200, 8, 9),
(7.00, 3000, 9, 9),
(20.00, 1000, 10, 9),
(10.00, 1500, 6, 10),
(0.30, 8000, 7, 10),
(25.00, 200, 8, 10),
(7.00, 3000, 9, 10),
(20.00, 1000, 10, 10),
(10.00, 1500, 6, 11),
(0.30, 8000, 7, 11),
(25.00, 200, 8, 11),
(7.00, 3000, 9, 11),
(20.00, 1000, 10, 11),
(10.00, 1500, 6, 12),
(0.30, 8000, 7, 12),
(25.00, 200, 8, 12),
(7.00, 3000, 9, 12),
(20.00, 1000, 10, 12),
(10.00, 1500, 6, 13),
(0.30, 8000, 7, 13),
(25.00, 200, 8, 13),
(7.00, 3000, 9, 13),
(20.00, 1000, 10, 13),
(10.00, 1500, 6, 14),
(0.30, 8000, 7, 14),
(25.00, 200, 8, 14),
(7.00, 3000, 9, 14),
(20.00, 1000, 10, 14),
(10.00, 1500, 6, 15),
(0.30, 8000, 7, 15),
(25.00, 200, 8, 15),
(7.00, 3000, 9, 15),
(20.00, 1000, 10, 15),
(10.00, 1500, 6, 16),
(0.30, 8000, 7, 16),
(25.00, 200, 8, 16),
(7.00, 3000, 9, 16),
(20.00, 1000, 10, 16),
(10.00, 1500, 6, 17),
(0.30, 8000, 7, 17),
(25.00, 200, 8, 17),
(7.00, 3000, 9, 17),
(20.00, 1000, 10, 17),
(10.00, 1500, 6, 18),
(0.30, 8000, 7, 18),
(25.00, 200, 8, 18),
(7.00, 3000, 9, 18),
(20.00, 1000, 10, 18),
(10.00, 1500, 6, 19),
(0.30, 8000, 7, 19),
(25.00, 200, 8, 19),
(7.00, 3000, 9, 19),
(20.00, 1000, 10, 19),
(10.00, 1500, 6, 20),
(0.30, 8000, 7, 20),
(25.00, 200, 8, 20),
(7.00, 3000, 9, 20),
(20.00, 1000, 10, 20);

-- =====================================================
-- 17. Insertar Compras de Materiales Adicionales
-- =====================================================

INSERT INTO COMPRA_MATERIAL (COSTO_TOTAL, FECHA, PROVEEDOR_ID, DETALLE) VALUES
(5000.00, '2024-02-10 10:00:00', 1, 'Compra de barras de refuerzo y tornillos.'),
(3000.00, '2024-05-15 11:30:00', 2, 'Compra de adhesivos y cables de energía.'),
(4000.00, '2024-08-20 09:45:00', 3, 'Compra de tuberías de acero y tornillos de madera.');

-- =====================================================
-- 18. Insertar Detalles de Compras de Materiales Adicionales
-- =====================================================

INSERT INTO DETALLE_COMPRA_MATERIAL (COSTO, CANTIDAD, MATERIAL_ID, COMPRA_MATERIAL_ID) VALUES
(10.00, 1500, 6, 6),
(0.30, 8000, 7, 6),
(25.00, 200, 8, 6),
(7.00, 3000, 9, 6),
(20.00, 1000, 10, 6),
(10.00, 1500, 6, 7),
(0.30, 8000, 7, 7),
(25.00, 200, 8, 7),
(7.00, 3000, 9, 7),
(20.00, 1000, 10, 7),
(10.00, 1500, 6, 8),
(0.30, 8000, 7, 8),
(25.00, 200, 8, 8),
(7.00, 3000, 9, 8),
(20.00, 1000, 10, 8),
(10.00, 1500, 6, 9),
(0.30, 8000, 7, 9),
(25.00, 200, 8, 9),
(7.00, 3000, 9, 9),
(20.00, 1000, 10, 9),
(10.00, 1500, 6, 10),
(0.30, 8000, 7, 10),
(25.00, 200, 8, 10),
(7.00, 3000, 9, 10),
(20.00, 1000, 10, 10),
(10.00, 1500, 6, 11),
(0.30, 8000, 7, 11),
(25.00, 200, 8, 11),
(7.00, 3000, 9, 11),
(20.00, 1000, 10, 11),
(10.00, 1500, 6, 12),
(0.30, 8000, 7, 12),
(25.00, 200, 8, 12),
(7.00, 3000, 9, 12),
(20.00, 1000, 10, 12),
(10.00, 1500, 6, 13),
(0.30, 8000, 7, 13),
(25.00, 200, 8, 13),
(7.00, 3000, 9, 13),
(20.00, 1000, 10, 13),
(10.00, 1500, 6, 14),
(0.30, 8000, 7, 14),
(25.00, 200, 8, 14),
(7.00, 3000, 9, 14),
(20.00, 1000, 10, 14),
(10.00, 1500, 6, 15),
(0.30, 8000, 7, 15),
(25.00, 200, 8, 15),
(7.00, 3000, 9, 15),
(20.00, 1000, 10, 15),
(10.00, 1500, 6, 16),
(0.30, 8000, 7, 16),
(25.00, 200, 8, 16),
(7.00, 3000, 9, 16),
(20.00, 1000, 10, 16),
(10.00, 1500, 6, 17),
(0.30, 8000, 7, 17),
(25.00, 200, 8, 17),
(7.00, 3000, 9, 17),
(20.00, 1000, 10, 17),
(10.00, 1500, 6, 18),
(0.30, 8000, 7, 18),
(25.00, 200, 8, 18),
(7.00, 3000, 9, 18),
(20.00, 1000, 10, 18),
(10.00, 1500, 6, 19),
(0.30, 8000, 7, 19),
(25.00, 200, 8, 19),
(7.00, 3000, 9, 19),
(20.00, 1000, 10, 19),
(10.00, 1500, 6, 20),
(0.30, 8000, 7, 20),
(25.00, 200, 8, 20),
(7.00, 3000, 9, 20),
(20.00, 1000, 10, 20);

-- =====================================================
-- 19. Insertar Uso de Materiales y Sobrantes para Proyectos
-- =====================================================

-- Uso de Materiales para Proyecto Gamma (ID=1)
INSERT INTO USO_MATERIAL (ASIGNACION_MATERIAL_ID, CANTIDAD, FECHA, DETALLE) VALUES
(1, 100, '2024-02-15', 'Uso de cemento en fundaciones.'),
(2, 200, '2024-02-20', 'Uso de arena para mezcla.'),
(3, 150, '2024-02-25', 'Uso de grava en estructuras.'),
(4, 50, '2024-03-01', 'Uso de varillas en refuerzos.');

-- Sobrantes para Proyecto Gamma (ID=1)
INSERT INTO SOBRANTE_PROYECTO (ASIGNACION_MATERIAL_ID, CANTIDAD) VALUES
(1, 400),
(2, 1800),
(3, 1350),
(4, 50);

-- Uso de Materiales para Proyecto Delta (ID=2)
INSERT INTO USO_MATERIAL (ASIGNACION_MATERIAL_ID, CANTIDAD, FECHA, DETALLE) VALUES
(5, 200, '2024-03-20', 'Uso de barras de refuerzo en estructuras.'),
(6, 400, '2024-03-25', 'Uso de tornillos en ensamblajes.'),
(7, 300, '2024-03-30', 'Uso de adhesivos en acabados.'),
(8, 100, '2024-04-05', 'Uso de cables en instalaciones eléctricas.');

-- Sobrantes para Proyecto Delta (ID=2)
INSERT INTO SOBRANTE_PROYECTO (ASIGNACION_MATERIAL_ID, CANTIDAD) VALUES
(5, 800),
(6, 3600),
(7, 2700),
(8, 900);

-- Uso de Materiales para Proyecto Epsilon (ID=3)
INSERT INTO USO_MATERIAL (ASIGNACION_MATERIAL_ID, CANTIDAD, FECHA, DETALLE) VALUES
(9, 300, '2024-04-20', 'Uso de materiales en cimentación.'),
(10, 600, '2024-04-25', 'Uso de materiales en estructuras.'),
(11, 450, '2024-04-30', 'Uso de materiales en acabados.'),
(12, 150, '2024-05-05', 'Uso de materiales en instalaciones.'),
(13, 250, '2024-05-10', 'Uso de materiales en inspecciones.');

-- Sobrantes para Proyecto Epsilon (ID=3)
INSERT INTO SOBRANTE_PROYECTO (ASIGNACION_MATERIAL_ID, CANTIDAD) VALUES
(9, 2700),
(10, 2400),
(11, 2550),
(12, 1350),
(13, 2250);

-- Uso de Materiales para Proyecto Zeta (ID=4)
INSERT INTO USO_MATERIAL (ASIGNACION_MATERIAL_ID, CANTIDAD, FECHA, DETALLE) VALUES
(14, 400, '2024-05-20', 'Uso de tornillos en construcción.'),
(15, 800, '2024-05-25', 'Uso de clavos en estructuras.'),
(16, 600, '2024-05-30', 'Uso de anclajes en cimentaciones.'),
(17, 200, '2024-06-05', 'Uso de masilla en acabados.');

-- Sobrantes para Proyecto Zeta (ID=4)
INSERT INTO SOBRANTE_PROYECTO (ASIGNACION_MATERIAL_ID, CANTIDAD) VALUES
(14, 3600),
(15, 4200),
(16, 4800),
(17, 1800);

-- =====================================================
-- 20. Insertar Reportes
-- =====================================================

INSERT INTO REPORTE (FECHA_CREACION, DETALLE, ENCARGADO_FINANZAS_ID, ENCARGADO_ALMACEN_ID) VALUES
('2024-02-20 10:00:00', 'Reporte mensual de materiales utilizados y sobrantes en Proyecto Gamma.', 1, 1),
('2024-05-20 15:30:00', 'Reporte trimestral de herramientas asignadas y usadas en Proyecto Delta.', 2, 2),
('2024-08-25 09:45:00', 'Reporte de inspección final de Proyecto Epsilon.', 3, 3),
('2024-11-30 14:15:00', 'Reporte anual de uso de materiales y herramientas en Proyecto Zeta.', 4, 4);
