/*
 Navicat Premium Data Transfer

 Source Server         : 我自己的机器
 Source Server Type    : MySQL
 Source Server Version : 50733
 Source Host           : localhost:3306
 Source Schema         : luffycity

 Target Server Type    : MySQL
 Target Server Version : 50733
 File Encoding         : 65001

 Date: 20/04/2022 01:00:25
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for men
-- ----------------------------
DROP TABLE IF EXISTS `men`;
CREATE TABLE `men`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `age` int(11) NULL DEFAULT NULL,
  `address` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of men
-- ----------------------------
INSERT INTO `men` VALUES (5, 'alex', 99, '鸡冠山');
INSERT INTO `men` VALUES (6, 'tory', 19, '八宝山');
INSERT INTO `men` VALUES (7, 'tory1', 19, '八宝山第一栋');
INSERT INTO `men` VALUES (8, 'tory2', 20, '八宝山第二栋');
INSERT INTO `men` VALUES (9, 'tory3', 21, '八宝山第二栋');
INSERT INTO `men` VALUES (10, 'tory4', 22, '八宝山第二栋');
INSERT INTO `men` VALUES (11, 'tory5', 23, '八宝山第二栋');
INSERT INTO `men` VALUES (12, 'tory6', 24, '八宝山第一栋');
INSERT INTO `men` VALUES (13, 'tory7', 25, '八宝山第一栋');
INSERT INTO `men` VALUES (14, 'tory8', 25, '八宝山第一栋');
INSERT INTO `men` VALUES (15, 'tory9', 24, '八宝山第一栋');
INSERT INTO `men` VALUES (17, '燕归来', 18, '八宝山');

-- ----------------------------
-- Table structure for person
-- ----------------------------
DROP TABLE IF EXISTS `person`;
CREATE TABLE `person`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `age` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `address` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of person
-- ----------------------------
INSERT INTO `person` VALUES (1, 'alex', '18', '0123');
INSERT INTO `person` VALUES (2, 'wusir', '99', '123123');
INSERT INTO `person` VALUES (3, '傻叉', '11', '1231');
INSERT INTO `person` VALUES (4, 'lsfdkjaklfj', '123', '12313');
INSERT INTO `person` VALUES (5, 'jfkdslaj', '2334', '234234');

-- ----------------------------
-- Table structure for stu
-- ----------------------------
DROP TABLE IF EXISTS `stu`;
CREATE TABLE `stu`  (
  `stu_no` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `gender` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `birthday` date NULL DEFAULT NULL,
  `addresss` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`stu_no`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2024 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of stu
-- ----------------------------
INSERT INTO `stu` VALUES (1, 'alex', '1', '2022-04-20', '北京八宝山');
INSERT INTO `stu` VALUES (3, '樵夫', '3', '2022-04-13', '北京八宝山');
INSERT INTO `stu` VALUES (4, 'fkjaskljfkalsj', '1', NULL, 'fjklasdjfklasj');
INSERT INTO `stu` VALUES (1989, '12312', '男', '2022-04-12', '123123');
INSERT INTO `stu` VALUES (2021, '1231231', '2', NULL, '12312312231');
INSERT INTO `stu` VALUES (2022, '12312312321', '123123', '2022-03-30', '123123213');
INSERT INTO `stu` VALUES (2023, '123123', '123', '2022-03-29', '123123');

SET FOREIGN_KEY_CHECKS = 1;
