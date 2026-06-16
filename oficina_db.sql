-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 16/06/2026 às 06:52
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `oficina.db`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `carro`
--

CREATE TABLE `carro` (
  `id` int(11) NOT NULL,
  `placa` varchar(10) DEFAULT NULL,
  `modelo` varchar(50) DEFAULT NULL,
  `marca` varchar(50) DEFAULT NULL,
  `cor` varchar(25) DEFAULT NULL,
  `ano` year(4) DEFAULT NULL,
  `id_cliente` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `carro`
--

INSERT INTO `carro` (`id`, `placa`, `modelo`, `marca`, `cor`, `ano`, `id_cliente`) VALUES
(0, 'Placa', 'Marca', 'Modelo', '0', '0000', 0),
(1, '123123', '21', '21', '2000', '2000', 0),
(6, 'm121mm', 'ram2500', 'ram', 'preto', '2001', 2),
(7, 'm121mm', 'ram2500', 'ram', 'preto', '2001', 2),
(8, 'Placa', 'Modelo', 'Marca', 'Cor', '0000', 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `cliente`
--

CREATE TABLE `cliente` (
  `id` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `cpf` varchar(14) DEFAULT NULL,
  `telefone` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `endereco` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `cliente`
--

INSERT INTO `cliente` (`id`, `nome`, `cpf`, `telefone`, `email`, `endereco`) VALUES
(1, 'renan', '01201201200', '67999999999', 'renan@gmail.com', 'rua da fiorela'),
(6, 'lucas', '012012012', '6799989898', 'lulu', 'rua 2'),
(7, 'Nome', 'CPF', 'Telefone', 'Email', 'Endereço');

-- --------------------------------------------------------

--
-- Estrutura para tabela `ordem_servico`
--

CREATE TABLE `ordem_servico` (
  `id` int(11) NOT NULL,
  `id_cliente` int(11) DEFAULT NULL,
  `id_carro` int(11) DEFAULT NULL,
  `data_abertura` datetime DEFAULT current_timestamp(),
  `status` varchar(20) DEFAULT 'aberta'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `ordem_servico`
--

INSERT INTO `ordem_servico` (`id`, `id_cliente`, `id_carro`, `data_abertura`, `status`) VALUES
(2, 1, 6, '2026-05-10 00:00:00', 'Em Andamento'),
(3, 1, 6, '2026-02-10 00:00:00', 'Em Andamento'),
(4, 6, 7, '0000-00-00 00:00:00', '2026-08-19 00:00:00');

-- --------------------------------------------------------

--
-- Estrutura para tabela `servico`
--

CREATE TABLE `servico` (
  `id` int(11) NOT NULL,
  `nome` varchar(100) DEFAULT NULL,
  `descricao` text DEFAULT NULL,
  `preco` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `servico`
--

INSERT INTO `servico` (`id`, `nome`, `descricao`, `preco`) VALUES
(1, 'll', 'painel', 100.00),
(4, 'luiz', 'troca', 100.00),
(5, 'renan ', 'limpeza', 150.00),
(6, 'll', 'painel', 100.00),
(7, 'Nome', 'Descrição', 0.00);

-- --------------------------------------------------------

--
-- Estrutura para tabela `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `login` varchar(100) NOT NULL,
  `senha` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `usuario`
--

INSERT INTO `usuario` (`id`, `login`, `senha`) VALUES
(1, 'lucas', '123456'),
(2, 'Enilda', 'Enilda123');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `carro`
--
ALTER TABLE `carro`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `ordem_servico`
--
ALTER TABLE `ordem_servico`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_cliente` (`id_cliente`),
  ADD KEY `id_carro` (`id_carro`);

--
-- Índices de tabela `servico`
--
ALTER TABLE `servico`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `carro`
--
ALTER TABLE `carro`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de tabela `cliente`
--
ALTER TABLE `cliente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de tabela `ordem_servico`
--
ALTER TABLE `ordem_servico`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `servico`
--
ALTER TABLE `servico`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de tabela `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `ordem_servico`
--
ALTER TABLE `ordem_servico`
  ADD CONSTRAINT `ordem_servico_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id`),
  ADD CONSTRAINT `ordem_servico_ibfk_2` FOREIGN KEY (`id_carro`) REFERENCES `carro` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
