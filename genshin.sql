-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 09, 2024 at 05:45 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `genshin`
--

-- --------------------------------------------------------

--
-- Table structure for table `buildchr`
--

CREATE TABLE `buildchr` (
  `id` int(3) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `artifact` varchar(100) NOT NULL,
  `weapon` varchar(100) NOT NULL,
  `main_stat` varchar(100) NOT NULL,
  `sub_stat` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `buildchr`
--

INSERT INTO `buildchr` (`id`, `nama`, `artifact`, `weapon`, `main_stat`, `sub_stat`) VALUES
(1, 'Zhongli', 'Tenacity of the Millelith x4', 'Black Tassel', 'HP%', 'HP%, HP, Energy Recharge');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `buildchr`
--
ALTER TABLE `buildchr`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `buildchr`
--
ALTER TABLE `buildchr`
  MODIFY `id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
