-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: csdlhangkhong
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `chuyenbay`
--

DROP TABLE IF EXISTS `chuyenbay`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chuyenbay` (
  `MaCB` char(5) COLLATE utf8_unicode_ci NOT NULL,
  `GaDi` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `GaDen` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `DoDai` int NOT NULL,
  `GioDi` time NOT NULL,
  `GioDen` time NOT NULL,
  `ChiPhi` int NOT NULL,
  UNIQUE KEY `MaCB` (`MaCB`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chuyenbay`
--

LOCK TABLES `chuyenbay` WRITE;
/*!40000 ALTER TABLE `chuyenbay` DISABLE KEYS */;
INSERT INTO `chuyenbay` VALUES ('10','HaNoi','Vinh',876,'20:54:56','19:07:43',964267),('15','Vinh','HaNoi',541,'19:27:24','01:18:30',593954),('17','Paris','HaNoi',588,'16:01:34','20:41:16',232590),('19','HaNoi','BangKok',645,'12:10:14','12:30:52',989351),('7','DaNang','HCM',879,'03:40:53','03:01:49',124052),('8','Paris','HaNoi',309,'13:04:18','17:20:14',596276),('9','BangKok','HCM',934,'08:43:11','12:11:15',612300),('a1','HaNoi','HCM',1000,'08:00:00','11:00:00',3000),('a2','DaNang','HCM',500,'12:00:00','13:30:00',1000),('a3','Vinh','HCM',650,'15:00:00','16:45:00',1200),('a4','Vinh','HaNoi',350,'15:00:00','16:00:00',1100),('a5','HaNoi','DaNang',675,'15:00:00','16:45:00',2000),('a6','HaNoi','DaNang',675,'08:00:00','10:00:00',2000);
/*!40000 ALTER TABLE `chuyenbay` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-16 21:34:55
