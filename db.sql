/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - bloodline_logistics
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`bloodline_logistics` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `bloodline_logistics`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_permission` */

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `bloodline_logistics_blood` */

DROP TABLE IF EXISTS `bloodline_logistics_blood`;

CREATE TABLE `bloodline_logistics_blood` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `blood_name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `bloodline_logistics_blood` */

insert  into `bloodline_logistics_blood`(`id`,`blood_name`) values (1,'A +ve'),(2,'A -ve');

/*Table structure for table `bloodline_logistics_blood_bank` */

DROP TABLE IF EXISTS `bloodline_logistics_blood_bank`;

CREATE TABLE `bloodline_logistics_blood_bank` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stock` varchar(100) NOT NULL,
  `BLOOD_ID_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `BloodLine_Logistics__BLOOD_ID_id_cc42c43c_fk_BloodLine` (`BLOOD_ID_id`),
  CONSTRAINT `BloodLine_Logistics__BLOOD_ID_id_cc42c43c_fk_BloodLine` FOREIGN KEY (`BLOOD_ID_id`) REFERENCES `bloodline_logistics_blood` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `bloodline_logistics_blood_bank` */

insert  into `bloodline_logistics_blood_bank`(`id`,`stock`,`BLOOD_ID_id`) values (1,'10',1),(2,'20',2);

/*Table structure for table `bloodline_logistics_donor` */

DROP TABLE IF EXISTS `bloodline_logistics_donor`;

CREATE TABLE `bloodline_logistics_donor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `house` varchar(100) NOT NULL,
  `pin` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `BLOOD_ID_id` int(11) NOT NULL,
  `LOGIN_id` int(11) NOT NULL,
  `age` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `BloodLine_Logistics__BLOOD_ID_id_d6af71bb_fk_BloodLine` (`BLOOD_ID_id`),
  KEY `BloodLine_Logistics__LOGIN_id_97f91129_fk_BloodLine` (`LOGIN_id`),
  CONSTRAINT `BloodLine_Logistics__BLOOD_ID_id_d6af71bb_fk_BloodLine` FOREIGN KEY (`BLOOD_ID_id`) REFERENCES `bloodline_logistics_blood` (`id`),
  CONSTRAINT `BloodLine_Logistics__LOGIN_id_97f91129_fk_BloodLine` FOREIGN KEY (`LOGIN_id`) REFERENCES `bloodline_logistics_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `bloodline_logistics_donor` */

insert  into `bloodline_logistics_donor`(`id`,`name`,`email`,`phone`,`house`,`pin`,`post`,`gender`,`BLOOD_ID_id`,`LOGIN_id`,`age`) values (1,'ananya','ananyakk2910@gmail.com','09876543219','thalassery','670213','Pinarayi','Female',1,2,'22'),(3,'vidya','vidyaraghunathan22@gmail.com','9876543210','rosevilla','670741','kannur','Male',1,5,'23');

/*Table structure for table `bloodline_logistics_feedback` */

DROP TABLE IF EXISTS `bloodline_logistics_feedback`;

CREATE TABLE `bloodline_logistics_feedback` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(100) NOT NULL,
  `feedback` varchar(100) NOT NULL,
  `LOGIN_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `BloodLine_Logistics__LOGIN_id_50c2f081_fk_BloodLine` (`LOGIN_id`),
  CONSTRAINT `BloodLine_Logistics__LOGIN_id_50c2f081_fk_BloodLine` FOREIGN KEY (`LOGIN_id`) REFERENCES `bloodline_logistics_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `bloodline_logistics_feedback` */

insert  into `bloodline_logistics_feedback`(`id`,`date`,`feedback`,`LOGIN_id`) values (1,'11-01-2024','Haiiii\r\n',2);

/*Table structure for table `bloodline_logistics_login` */

DROP TABLE IF EXISTS `bloodline_logistics_login`;

CREATE TABLE `bloodline_logistics_login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `usertype` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `bloodline_logistics_login` */

insert  into `bloodline_logistics_login`(`id`,`username`,`password`,`usertype`) values (1,'admin','admin','admin'),(2,'ananyakk2910@gmail.com','ananya','donor'),(3,'bob@gmail.com','bob','seeker'),(5,'vidyaraghunathan22@gmail.com','vidyaa','donor');

/*Table structure for table `bloodline_logistics_request` */

DROP TABLE IF EXISTS `bloodline_logistics_request`;

CREATE TABLE `bloodline_logistics_request` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `status` varchar(100) NOT NULL,
  `BLOOD_ID_id` int(11) NOT NULL,
  `SEEKER_id` int(11) NOT NULL,
  `quantity` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `BloodLine_Logistics__BLOOD_ID_id_4291558a_fk_BloodLine` (`BLOOD_ID_id`),
  KEY `BloodLine_Logistics__SEEKER_id_b9fa0fa0_fk_BloodLine` (`SEEKER_id`),
  CONSTRAINT `BloodLine_Logistics__BLOOD_ID_id_4291558a_fk_BloodLine` FOREIGN KEY (`BLOOD_ID_id`) REFERENCES `bloodline_logistics_blood` (`id`),
  CONSTRAINT `BloodLine_Logistics__SEEKER_id_b9fa0fa0_fk_BloodLine` FOREIGN KEY (`SEEKER_id`) REFERENCES `bloodline_logistics_seeker` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `bloodline_logistics_request` */

insert  into `bloodline_logistics_request`(`id`,`date`,`status`,`BLOOD_ID_id`,`SEEKER_id`,`quantity`) values (1,'2024-01-11','pending',1,1,'');

/*Table structure for table `bloodline_logistics_request_allocation` */

DROP TABLE IF EXISTS `bloodline_logistics_request_allocation`;

CREATE TABLE `bloodline_logistics_request_allocation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` varchar(100) NOT NULL,
  `DONOR_id` int(11) NOT NULL,
  `REQUEST_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `BloodLine_Logistics__DONOR_id_80d43e75_fk_BloodLine` (`DONOR_id`),
  KEY `BloodLine_Logistics__REQUEST_id_13f07df8_fk_BloodLine` (`REQUEST_id`),
  CONSTRAINT `BloodLine_Logistics__REQUEST_id_13f07df8_fk_BloodLine` FOREIGN KEY (`REQUEST_id`) REFERENCES `bloodline_logistics_request` (`id`),
  CONSTRAINT `BloodLine_Logistics__DONOR_id_80d43e75_fk_BloodLine` FOREIGN KEY (`DONOR_id`) REFERENCES `bloodline_logistics_donor` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `bloodline_logistics_request_allocation` */

/*Table structure for table `bloodline_logistics_seeker` */

DROP TABLE IF EXISTS `bloodline_logistics_seeker`;

CREATE TABLE `bloodline_logistics_seeker` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `BLOOD_ID_id` int(11) NOT NULL,
  `LOGIN_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `BloodLine_Logistics__BLOOD_ID_id_64ce594a_fk_BloodLine` (`BLOOD_ID_id`),
  KEY `BloodLine_Logistics__LOGIN_id_70ca3bea_fk_BloodLine` (`LOGIN_id`),
  CONSTRAINT `BloodLine_Logistics__LOGIN_id_70ca3bea_fk_BloodLine` FOREIGN KEY (`LOGIN_id`) REFERENCES `bloodline_logistics_login` (`id`),
  CONSTRAINT `BloodLine_Logistics__BLOOD_ID_id_64ce594a_fk_BloodLine` FOREIGN KEY (`BLOOD_ID_id`) REFERENCES `bloodline_logistics_blood` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `bloodline_logistics_seeker` */

insert  into `bloodline_logistics_seeker`(`id`,`name`,`email`,`phone`,`gender`,`BLOOD_ID_id`,`LOGIN_id`) values (1,'bob','bob@gmail.com','09876543211','Male',1,3);

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_content_type` */

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_migrations` */

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('o3cl0dq7z930tp9csekzl4dzdyekiu7c','ZTk3MWMxNGUzYzcwMWY0YzRmNjY3NDllMDExMzFjNDgzZjhjODg0ODp7fQ==','2024-01-25 05:19:34.025441');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
