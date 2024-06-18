-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 09, 2023 at 04:34 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `book_rental`
--

-- --------------------------------------------------------

--
-- Table structure for table `admins`
--

CREATE TABLE `admins` (
  `id` int(11) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `username` varchar(25) DEFAULT NULL,
  `password` varchar(300) DEFAULT NULL,
  `access` varchar(50) DEFAULT NULL,
  `active` varchar(1) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admins`
--

INSERT INTO `admins` (`id`, `email`, `username`, `password`, `access`, `active`, `created_at`, `updated_at`) VALUES
(13, 'zhie@caz.com', 'admin', 'md5$XzejQa4EftFFVOXI$86d7ec17184bab6647cb65206e555751', 'developer', '1', '2023-12-01 00:00:55', '2023-12-01 00:00:55'),
(14, 'jigem18@gmail.com', 'jigem', 'md5$gEmpKYlhWzIWW49E$393c6c65b8a8fbea9a477f791bf35a31', 'developer', '1', '2023-12-01 00:00:55', '2023-12-01 00:00:55'),
(15, 'agunodkrista@gmail.com', 'rissi', 'md5$MBaRKz87xnvTXJzZ$737313099e660878ac0eee7dd4008b89', 'developer', '1', '2023-12-01 00:00:55', '2023-12-01 00:00:55'),
(16, 'joy@gmail.com', 'joy', 'md5$BQM9jYX3VIupAgeU$6338b28aa84a2d794337a8f93e137f38', 'developer', '1', '2023-12-01 00:00:55', '2023-12-01 00:00:55');

-- --------------------------------------------------------

--
-- Table structure for table `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('f963b9e7bddb');

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `id` int(11) NOT NULL,
  `title` varchar(300) DEFAULT NULL,
  `genre` varchar(30) DEFAULT NULL,
  `cast` mediumtext DEFAULT NULL,
  `img` mediumtext DEFAULT NULL,
  `amount` varchar(1000) DEFAULT NULL,
  `qty` varchar(255) NOT NULL,
  `available` varchar(1000) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`id`, `title`, `genre`, `cast`, `img`, `amount`, `qty`, `available`, `created_at`, `updated_at`) VALUES
(18, 'After The Chains', 'Romance', 'Jonaxx', 'C:\\fakepath\\after_the_chains.jpg', '150', '15', '13', '2023-12-04 22:04:04', '2023-12-09 22:25:45'),
(22, 'Kissing the dust', 'Romance', 'Jonaxx', 'C:\\fakepath\\kissing_the_dust.jpg', '50', '6', '0', '2023-12-04 22:26:49', '2023-12-04 22:59:38');

-- --------------------------------------------------------

--
-- Table structure for table `history`
--

CREATE TABLE `history` (
  `id` int(11) NOT NULL,
  `request_code` varchar(20) DEFAULT NULL,
  `book_id` varchar(20) DEFAULT NULL,
  `user_id` varchar(20) DEFAULT NULL,
  `duration` varchar(4) DEFAULT NULL,
  `collected` varchar(15) DEFAULT NULL,
  `remark` varchar(15) DEFAULT NULL,
  `remark_date` varchar(150) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `status`
--

CREATE TABLE `status` (
  `id` int(11) NOT NULL,
  `request_code` varchar(500) DEFAULT NULL,
  `user_id` varchar(150) DEFAULT NULL,
  `book_id_requested` varchar(500) DEFAULT NULL,
  `requested_date` varchar(500) DEFAULT NULL,
  `requested_quantity` int(255) NOT NULL,
  `requested_amount` int(255) NOT NULL,
  `status` varchar(500) DEFAULT NULL,
  `is_delete` varchar(255) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `firstname` varchar(25) DEFAULT NULL,
  `middlename` varchar(25) DEFAULT NULL,
  `lastname` varchar(25) DEFAULT NULL,
  `address` varchar(300) DEFAULT NULL,
  `contact_no` varchar(25) DEFAULT NULL,
  `verify` varchar(25) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `email`, `firstname`, `middlename`, `lastname`, `address`, `contact_no`, `verify`, `created_at`, `updated_at`) VALUES
(12, 'aj@gmail.com', 'April Joy', 'Caro', 'Lintao', 'Libertad', '09275810320', '1', '2023-12-01 09:34:39', '2023-12-01 09:34:39'),
(13, 'shmn@gmail.com', 'Shamon', 'Liboon', 'Salvaloza', 'Libertad', '09275810320', '1', '2023-12-01 09:34:39', '2023-12-01 09:34:39'),
(14, 'juswa@gmail.com', 'Joshua ', 'Kuizon', 'Gemima', 'Brgy. 4, Buenavista', '09064741708', '1', '2023-12-09 22:25:45', '2023-12-09 22:25:45');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admins`
--
ALTER TABLE `admins`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `history`
--
ALTER TABLE `history`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `status`
--
ALTER TABLE `status`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admins`
--
ALTER TABLE `admins`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `books`
--
ALTER TABLE `books`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `history`
--
ALTER TABLE `history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `status`
--
ALTER TABLE `status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
