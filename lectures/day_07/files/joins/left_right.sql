-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema left_right
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema left_right
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `left_right` DEFAULT CHARACTER SET utf8 ;
USE `left_right` ;

-- -----------------------------------------------------
-- Table `left_right`.`lefts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `left_right`.`lefts` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `left_name` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT now(),
  `updated_at` DATETIME NULL DEFAULT now() on update now(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `left_right`.`rights`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `left_right`.`rights` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `right_name` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT now(),
  `updated_at` DATETIME NULL DEFAULT now() on update now(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `left_right`.`left_right`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `left_right`.`left_right` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `right_id` INT NOT NULL,
  `left_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_left_right_rights_idx` (`right_id` ASC) VISIBLE,
  INDEX `fk_left_right_lefts1_idx` (`left_id` ASC) VISIBLE,
  CONSTRAINT `fk_left_right_rights`
    FOREIGN KEY (`right_id`)
    REFERENCES `left_right`.`rights` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_left_right_lefts1`
    FOREIGN KEY (`left_id`)
    REFERENCES `left_right`.`lefts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
