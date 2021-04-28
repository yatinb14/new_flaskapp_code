-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 19, 2021 at 07:23 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flasktab`
--

-- --------------------------------------------------------

--
-- Table structure for table `app`
--

CREATE TABLE `app` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `gstin` varchar(20) DEFAULT NULL,
  `pan` varchar(12) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app`
--

INSERT INTO `app` (`id`, `name`, `address`, `gstin`, `pan`, `email`) VALUES
(2, 'Yatin bhatia faridabad', '2e/137 nit', '1234567890QWER4', 'CHGPB1123G', 'ybhatia128@gmail.com'),
(3, 'Yatin bhatia 2', '2E/137 NIT FBD, Nit 2', '12345QWERTZXCVF', '1234ASDFGH', 'ybhatia128@gmail.com'),
(4, 'Yatin 5', 'nit 2', '1234567890QWERP', 'CHGPB1123X', 'ybhatia128@gmail.com'),
(5, 'Yatin bhatia 521', '2E/137 NIT FBD, Nit 2', '1234567890QWER9', 'CHGPB1123G', 'ybhatia128@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `expenses`
--

CREATE TABLE `expenses` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `description` varchar(150) DEFAULT NULL,
  `file` varchar(255) DEFAULT NULL,
  `dated` date DEFAULT NULL,
  `amount` float DEFAULT NULL,
  `status` varchar(20) NOT NULL DEFAULT 'Pending'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `expenses`
--

INSERT INTO `expenses` (`id`, `name`, `description`, `file`, `dated`, `amount`, `status`) VALUES
(1, 'Yatin bhatia', 'Fork from https://javascript.info/function-basics', '<FileStorage: \'art4.jpg\' (\'image/jpeg\')>', '2020-11-09', 445, 'Reject'),
(3, 'Atul', 'Laptop', '<FileStorage: \'art4.jpg\' (\'image/jpeg\')>', '2020-11-17', 45, 'Approved'),
(5, 'Atul', 'yyyyyyyyyyyyyyyyyyyyyyyyy', '<FileStorage: \'ioooo.txt\' (\'text/plain\')>', '2020-12-01', 67, 'Pending'),
(6, 'Atul', 'bbbbbbbbbbb', '<FileStorage: \'silver.html\' (\'text/html\')>', '2020-12-01', 78, 'Pending'),
(7, 'Atul', 'bbbbbbbbbbb', '<FileStorage: \'silver.html\' (\'text/html\')>', '2020-12-01', 78, 'Pending'),
(8, 'Atul', 'bbbbbbbbbbb', '<FileStorage: \'silver.html\' (\'text/html\')>', '2020-12-01', 78, 'Pending'),
(9, 'Atul', 'bbbbbbbbbbb', '<FileStorage: \'silver.html\' (\'text/html\')>', '2020-12-01', 78, 'Pending');

-- --------------------------------------------------------

--
-- Table structure for table `invoice`
--

CREATE TABLE `invoice` (
  `id` int(10) UNSIGNED NOT NULL,
  `num` int(11) DEFAULT NULL,
  `dated` datetime DEFAULT NULL,
  `unitcost` varchar(10) DEFAULT NULL,
  `qty` int(5) DEFAULT NULL,
  `pric` varchar(10) DEFAULT NULL,
  `item` varchar(20) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `total` varchar(10) DEFAULT NULL,
  `subtotal` int(10) DEFAULT NULL,
  `paid` int(10) DEFAULT NULL,
  `balance` varchar(10) DEFAULT NULL,
  `name` varchar(15) DEFAULT NULL,
  `ad` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `invoiced`
--

CREATE TABLE `invoiced` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `ad` varchar(20) DEFAULT NULL,
  `gst` varchar(25) DEFAULT NULL,
  `pan` varchar(15) DEFAULT NULL,
  `train` varchar(30) NOT NULL,
  `num` varchar(15) DEFAULT NULL,
  `dated` date DEFAULT NULL,
  `item` varchar(20) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `total` float DEFAULT NULL,
  `subtotal` float DEFAULT NULL,
  `words` varchar(50) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `newgst` varchar(10) NOT NULL,
  `status` varchar(15) DEFAULT 'open',
  `poid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `invoiced`
--

INSERT INTO `invoiced` (`id`, `name`, `ad`, `gst`, `pan`, `train`, `num`, `dated`, `item`, `description`, `total`, `subtotal`, `words`, `email`, `newgst`, `status`, `poid`) VALUES
(23, 'Yatin bhatia faridabad', '2e/137 nit', '1234567890qwer4  ', '  Chgpb1123g', 'None', 'INA5001', '2020-11-17', NULL, NULL, 50, 59, 'Fifty Nine Rupees only', 'ybhatia128@gmail.com  ', '9.00', 'Open', NULL),
(25, 'Yatin bhatia', '2e/137 nit', '1234567890qwert', 'Chgpb1123g', 'None', 'INTH2004/20-21', '2020-11-23', NULL, NULL, 23, 27.14, 'Twenty Seven Rupees only', 'ybhatia128@gmail.com', '4.14', 'open', NULL),
(26, '3', '2e/137 nit fbd, nit ', '12345qwertzxcvf', '1234asdfgh', 'Python', 'INTH2007/20-21', '2020-11-26', NULL, NULL, 89, 105.02, 'One Hundred Five Rupees only', 'ybhatia128@gmail.com', '16.02', 'open', 25),
(27, '4', 'Nit 2', '1234567890qwerp', 'Chgpb1123x', 'Python', 'INTH3005/20-21', '2020-11-26', NULL, NULL, 178, 210.04, 'Two Hundred Ten Rupees only', 'ybhatia128@gmail.com', '32.04', 'Closed', 26),
(28, '3', '2e/137 nit fbd, nit ', '12345qwertzxcvf', '1234asdfgh', 'Python', 'INTH2001/20-21', '2020-11-26', NULL, NULL, 78, 92.04, 'Ninety Two Rupees only ', 'ybhatia128@gmail.com', '14.04', 'Closed', 25);

-- --------------------------------------------------------

--
-- Table structure for table `invoiceorders`
--

CREATE TABLE `invoiceorders` (
  `orderid` int(10) UNSIGNED NOT NULL,
  `invoiceid` int(10) UNSIGNED DEFAULT NULL,
  `item` varchar(40) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `unitcost` int(10) NOT NULL,
  `quantity` int(10) NOT NULL,
  `price` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `invoiceorders`
--

INSERT INTO `invoiceorders` (`orderid`, `invoiceid`, `item`, `description`, `unitcost`, `quantity`, `price`) VALUES
(17, 23, 'Item Name', 'Description   ', 5, 1, 'Rs5.00  '),
(18, 23, 'Item Name 3', 'Description  ', 45, 1, 'Rs45.00'),
(19, 25, 'Item Name', 'IBM Online Training', 23, 1, 'Rs23.00'),
(20, 26, 'Item Name', 'Description ', 89, 1, 'Rs89.00'),
(23, 28, 'Item Name', 'Description  ', 78, 1, 'Rs78.00 '),
(24, 27, 'Item Name', 'Description  ', 89, 2, 'Rs178.00');

-- --------------------------------------------------------

--
-- Table structure for table `newrecieved`
--

CREATE TABLE `newrecieved` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `ad` varchar(20) DEFAULT NULL,
  `gst` varchar(25) DEFAULT NULL,
  `pan` varchar(15) DEFAULT NULL,
  `file` varchar(255) DEFAULT NULL,
  `num` varchar(15) DEFAULT NULL,
  `dated` date DEFAULT NULL,
  `item` varchar(20) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `total` float DEFAULT NULL,
  `subtotal` float DEFAULT NULL,
  `words` varchar(50) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `newgst` varchar(10) NOT NULL,
  `status` varchar(15) NOT NULL DEFAULT 'open'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `newrecieved`
--

INSERT INTO `newrecieved` (`id`, `name`, `ad`, `gst`, `pan`, `file`, `num`, `dated`, `item`, `description`, `total`, `subtotal`, `words`, `email`, `newgst`, `status`) VALUES
(19, 'Yatin bhatia trainer', NULL, 'null', 'null', '<FileStorage: \'aws1.jpg\' (\'image/jpeg\')>', 'INTH2005/20-21', '2020-12-01', NULL, NULL, 89, 105.02, 'One Hundred Five Rupees only ', NULL, '16.02', 'Open');

-- --------------------------------------------------------

--
-- Table structure for table `newrecievedorders`
--

CREATE TABLE `newrecievedorders` (
  `orderid` int(10) UNSIGNED NOT NULL,
  `prid` int(10) UNSIGNED DEFAULT NULL,
  `item` varchar(40) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `unitcost` float NOT NULL,
  `quantity` float NOT NULL,
  `price` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `newrecievedorders`
--

INSERT INTO `newrecievedorders` (`orderid`, `prid`, `item`, `description`, `unitcost`, `quantity`, `price`) VALUES
(2, 19, 'Item Name', 'Description  ', 89, 1, 'Rs89.00 ');

-- --------------------------------------------------------

--
-- Table structure for table `purchase`
--

CREATE TABLE `purchase` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `ad` varchar(20) DEFAULT NULL,
  `gst` varchar(25) DEFAULT NULL,
  `pan` varchar(15) DEFAULT NULL,
  `train` varchar(30) NOT NULL,
  `num` varchar(15) DEFAULT NULL,
  `dated` date DEFAULT NULL,
  `item` varchar(20) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `total` float DEFAULT NULL,
  `subtotal` float DEFAULT NULL,
  `words` varchar(50) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `newgst` varchar(10) NOT NULL,
  `status` varchar(15) NOT NULL DEFAULT 'open',
  `fromdate` date NOT NULL,
  `todate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `purchase`
--

INSERT INTO `purchase` (`id`, `name`, `ad`, `gst`, `pan`, `train`, `num`, `dated`, `item`, `description`, `total`, `subtotal`, `words`, `email`, `newgst`, `status`, `fromdate`, `todate`) VALUES
(23, '2', '2e/137 nit', '1234567890QWER4', 'CHGPB1123G', 'None', 'INA0401', '2020-10-31', NULL, NULL, 0, 0, '  ', 'ybhatia128@gmail.com', '0.0', 'Closed', '0000-00-00', '0000-00-00'),
(24, 'Yatin bhatia 2', '112', '1234567890qwert ', ' Chgpb1123g', 'Python', 'INTH2005/20-21', '2020-11-25', NULL, NULL, 67, 79.06, 'Seventy Nine Rupees only ', 'ybhatia128@gmail.com ', '12.06', 'Open', '2020-11-05', '2020-12-25'),
(25, '3', '112', '12345qwertzxcvf', '1234asdfgh', 'Python', 'INTH2007/20-21', '2020-11-26', NULL, NULL, 78, 92.04, 'Ninety Two Rupees only ', 'ybhatia128@gmail.com', '14.04', 'Closed', '2020-11-05', '2020-11-27');

-- --------------------------------------------------------

--
-- Table structure for table `purchaseorders`
--

CREATE TABLE `purchaseorders` (
  `orderid` int(10) UNSIGNED NOT NULL,
  `purchaseid` int(10) UNSIGNED DEFAULT NULL,
  `item` varchar(40) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `unitcost` int(10) NOT NULL,
  `quantity` int(10) NOT NULL,
  `price` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `purchaseorders`
--

INSERT INTO `purchaseorders` (`orderid`, `purchaseid`, `item`, `description`, `unitcost`, `quantity`, `price`) VALUES
(5, 24, 'Item Name', 'Description  ', 67, 1, 'Rs67.00 '),
(8, 23, 'Item Name', 'Description  ', 0, 1, 'Rs 0.0  '),
(10, 25, 'Item Name', 'Description  ', 78, 1, 'Rs78.00 ');

-- --------------------------------------------------------

--
-- Table structure for table `recieved`
--

CREATE TABLE `recieved` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `ad` varchar(20) DEFAULT NULL,
  `gst` varchar(25) DEFAULT NULL,
  `pan` varchar(15) DEFAULT NULL,
  `file` varchar(255) DEFAULT NULL,
  `num` varchar(15) DEFAULT NULL,
  `dated` date DEFAULT NULL,
  `item` varchar(20) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `total` float DEFAULT NULL,
  `subtotal` float DEFAULT NULL,
  `words` varchar(50) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `newgst` varchar(10) NOT NULL,
  `status` varchar(15) NOT NULL DEFAULT 'open'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `recieved`
--

INSERT INTO `recieved` (`id`, `name`, `ad`, `gst`, `pan`, `file`, `num`, `dated`, `item`, `description`, `total`, `subtotal`, `words`, `email`, `newgst`, `status`) VALUES
(19, 'Yatin bhatia trainer', NULL, 'Null ', ' Null', '<FileStorage: \'aws1.jpg\' (\'image/jpeg\')>', 'INTH2065/20-21', '2020-12-01', NULL, NULL, 78, 92.04, 'Ninety Two Rupees only ', NULL, '14.04', 'Open');

-- --------------------------------------------------------

--
-- Table structure for table `recievedorders`
--

CREATE TABLE `recievedorders` (
  `orderid` int(10) UNSIGNED NOT NULL,
  `irid` int(10) UNSIGNED DEFAULT NULL,
  `item` varchar(40) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `unitcost` int(10) NOT NULL,
  `quantity` int(10) NOT NULL,
  `price` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `recievedorders`
--

INSERT INTO `recievedorders` (`orderid`, `irid`, `item`, `description`, `unitcost`, `quantity`, `price`) VALUES
(8, 19, 'Item Name', 'Description  new', 78, 1, 'Rs78.00 ');

-- --------------------------------------------------------

--
-- Table structure for table `trainer`
--

CREATE TABLE `trainer` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `trainertype` varchar(20) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `gstin` varchar(20) DEFAULT NULL,
  `pan` varchar(12) DEFAULT NULL,
  `acc1` varchar(40) DEFAULT NULL,
  `acc2` varchar(40) DEFAULT NULL,
  `acc3` varchar(40) DEFAULT NULL,
  `acc4` varchar(40) DEFAULT NULL,
  `tech1` varchar(60) DEFAULT NULL,
  `tech2` varchar(60) DEFAULT NULL,
  `tech3` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `trainer`
--

INSERT INTO `trainer` (`id`, `name`, `trainertype`, `status`, `gstin`, `pan`, `acc1`, `acc2`, `acc3`, `acc4`, `tech1`, `tech2`, `tech3`) VALUES
(3, 'Yatin bhatia 1', 'Internal', 'N/a', NULL, NULL, NULL, NULL, NULL, NULL, 'tyyyy', 'form', 'cloud');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `password` varchar(40) DEFAULT NULL,
  `usertype` varchar(10) NOT NULL,
  `status` int(3) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `password`, `usertype`, `status`) VALUES
(13, 'admin', 'admin@thinknyx.com', 'password@123', 'admin', 1),
(15, 'Yatin Bhatia', 'ybhatia128@gmail.com', 'yo@123', 'user', 1),
(18, 'Roopam', 'roopam.g@gmail.com', 'yo@123', 'user', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `app`
--
ALTER TABLE `app`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `expenses`
--
ALTER TABLE `expenses`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `invoice`
--
ALTER TABLE `invoice`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `invoiced`
--
ALTER TABLE `invoiced`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `invoiceorders`
--
ALTER TABLE `invoiceorders`
  ADD PRIMARY KEY (`orderid`),
  ADD KEY `invoiceid` (`invoiceid`);

--
-- Indexes for table `newrecieved`
--
ALTER TABLE `newrecieved`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newrecievedorders`
--
ALTER TABLE `newrecievedorders`
  ADD PRIMARY KEY (`orderid`),
  ADD KEY `prid` (`prid`);

--
-- Indexes for table `purchase`
--
ALTER TABLE `purchase`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `purchaseorders`
--
ALTER TABLE `purchaseorders`
  ADD PRIMARY KEY (`orderid`),
  ADD KEY `purchaseid` (`purchaseid`);

--
-- Indexes for table `recieved`
--
ALTER TABLE `recieved`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `recievedorders`
--
ALTER TABLE `recievedorders`
  ADD PRIMARY KEY (`orderid`),
  ADD KEY `irid` (`irid`);

--
-- Indexes for table `trainer`
--
ALTER TABLE `trainer`
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
-- AUTO_INCREMENT for table `app`
--
ALTER TABLE `app`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `expenses`
--
ALTER TABLE `expenses`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `invoice`
--
ALTER TABLE `invoice`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `invoiced`
--
ALTER TABLE `invoiced`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `invoiceorders`
--
ALTER TABLE `invoiceorders`
  MODIFY `orderid` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `newrecieved`
--
ALTER TABLE `newrecieved`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `newrecievedorders`
--
ALTER TABLE `newrecievedorders`
  MODIFY `orderid` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `purchase`
--
ALTER TABLE `purchase`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `purchaseorders`
--
ALTER TABLE `purchaseorders`
  MODIFY `orderid` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `recieved`
--
ALTER TABLE `recieved`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `recievedorders`
--
ALTER TABLE `recievedorders`
  MODIFY `orderid` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `trainer`
--
ALTER TABLE `trainer`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `invoiceorders`
--
ALTER TABLE `invoiceorders`
  ADD CONSTRAINT `invoiceorders_ibfk_1` FOREIGN KEY (`invoiceid`) REFERENCES `invoiced` (`id`);

--
-- Constraints for table `newrecievedorders`
--
ALTER TABLE `newrecievedorders`
  ADD CONSTRAINT `newrecievedorders_ibfk_1` FOREIGN KEY (`prid`) REFERENCES `newrecieved` (`id`);

--
-- Constraints for table `purchaseorders`
--
ALTER TABLE `purchaseorders`
  ADD CONSTRAINT `purchaseorders_ibfk_1` FOREIGN KEY (`purchaseid`) REFERENCES `purchase` (`id`);

--
-- Constraints for table `recievedorders`
--
ALTER TABLE `recievedorders`
  ADD CONSTRAINT `recievedorders_ibfk_1` FOREIGN KEY (`irid`) REFERENCES `recieved` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
