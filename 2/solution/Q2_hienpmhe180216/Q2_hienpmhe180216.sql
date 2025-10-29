USE [master]
GO
/****** Object:  Database [Q2_hienpmhe180216]    Script Date: 25/10/2025 18:19:29 ******/
CREATE DATABASE [Q2_hienpmhe180216]
GO
ALTER DATABASE [Q2_hienpmhe180216] SET COMPATIBILITY_LEVEL = 160
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [Q2_hienpmhe180216].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [Q2_hienpmhe180216] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [Q2_hienpmhe180216] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [Q2_hienpmhe180216] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [Q2_hienpmhe180216] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [Q2_hienpmhe180216] SET ARITHABORT OFF 
GO
ALTER DATABASE [Q2_hienpmhe180216] SET AUTO_CLOSE ON 
GO
ALTER DATABASE [Q2_hienpmhe180216] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [Q2_hienpmhe180216] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [Q2_hienpmhe180216] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [Q2_hienpmhe180216] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [Q2_hienpmhe180216] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [Q2_hienpmhe180216] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [Q2_hienpmhe180216] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [Q2_hienpmhe180216] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [Q2_hienpmhe180216] SET  ENABLE_BROKER 
GO
ALTER DATABASE [Q2_hienpmhe180216] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [Q2_hienpmhe180216] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [Q2_hienpmhe180216] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [Q2_hienpmhe180216] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [Q2_hienpmhe180216] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [Q2_hienpmhe180216] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [Q2_hienpmhe180216] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [Q2_hienpmhe180216] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [Q2_hienpmhe180216] SET  MULTI_USER 
GO
ALTER DATABASE [Q2_hienpmhe180216] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [Q2_hienpmhe180216] SET DB_CHAINING OFF 
GO
ALTER DATABASE [Q2_hienpmhe180216] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [Q2_hienpmhe180216] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [Q2_hienpmhe180216] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [Q2_hienpmhe180216] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
EXEC sys.sp_db_vardecimal_storage_format N'Q2_hienpmhe180216', N'ON'
GO
ALTER DATABASE [Q2_hienpmhe180216] SET QUERY_STORE = ON
GO
ALTER DATABASE [Q2_hienpmhe180216] SET QUERY_STORE (OPERATION_MODE = READ_WRITE, CLEANUP_POLICY = (STALE_QUERY_THRESHOLD_DAYS = 30), DATA_FLUSH_INTERVAL_SECONDS = 900, INTERVAL_LENGTH_MINUTES = 60, MAX_STORAGE_SIZE_MB = 1000, QUERY_CAPTURE_MODE = AUTO, SIZE_BASED_CLEANUP_MODE = AUTO, MAX_PLANS_PER_QUERY = 200, WAIT_STATS_CAPTURE_MODE = ON)
GO
USE [Q2_hienpmhe180216]
GO
/****** Object:  Table [dbo].[AccountMember]    Script Date: 25/10/2025 18:19:30 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[AccountMember](
	[MemberID] [nvarchar](20) NOT NULL,
	[MemberPassword] [nvarchar](80) NOT NULL,
	[FullName] [nvarchar](80) NOT NULL,
	[EmailAddress] [nvarchar](100) NOT NULL,
	[MemberRole] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[MemberID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Categories]    Script Date: 25/10/2025 18:19:30 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Categories](
	[CategoryID] [int] IDENTITY(1,1) NOT NULL,
	[CategoryName] [nvarchar](15) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[CategoryID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Products]    Script Date: 25/10/2025 18:19:30 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Products](
	[ProductID] [int] IDENTITY(1,1) NOT NULL,
	[ProductName] [nvarchar](40) NOT NULL,
	[CategoryID] [int] NOT NULL,
	[UnitsInStock] [smallint] NULL,
	[UnitPrice] [money] NULL,
PRIMARY KEY CLUSTERED 
(
	[ProductID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
INSERT [dbo].[AccountMember] ([MemberID], [MemberPassword], [FullName], [EmailAddress], [MemberRole]) VALUES (N'admin01', N'Admin@123', N'Nguyễn Văn Admin', N'admin@example.com', 1)
INSERT [dbo].[AccountMember] ([MemberID], [MemberPassword], [FullName], [EmailAddress], [MemberRole]) VALUES (N'cust01', N'Cust@123', N'Trần Văn Khách', N'customer1@example.com', 3)
INSERT [dbo].[AccountMember] ([MemberID], [MemberPassword], [FullName], [EmailAddress], [MemberRole]) VALUES (N'cust02', N'Cust@456', N'Phạm Thị Mai', N'customer2@example.com', 3)
INSERT [dbo].[AccountMember] ([MemberID], [MemberPassword], [FullName], [EmailAddress], [MemberRole]) VALUES (N'staff01', N'Staff@123', N'Lê Thị Nhân Viên', N'staff@example.com', 2)
GO
SET IDENTITY_INSERT [dbo].[Categories] ON 

INSERT [dbo].[Categories] ([CategoryID], [CategoryName]) VALUES (3, N'Điện thoại')
INSERT [dbo].[Categories] ([CategoryID], [CategoryName]) VALUES (4, N'Laptop')
INSERT [dbo].[Categories] ([CategoryID], [CategoryName]) VALUES (5, N'Phụ kiện')
INSERT [dbo].[Categories] ([CategoryID], [CategoryName]) VALUES (6, N'Home')
SET IDENTITY_INSERT [dbo].[Categories] OFF
GO
SET IDENTITY_INSERT [dbo].[Products] ON 

INSERT [dbo].[Products] ([ProductID], [ProductName], [CategoryID], [UnitsInStock], [UnitPrice]) VALUES (3, N'iPhone 15 Pro Max', 3, 15, 35000000.0000)
INSERT [dbo].[Products] ([ProductID], [ProductName], [CategoryID], [UnitsInStock], [UnitPrice]) VALUES (4, N'Samsung Galaxy S24', 3, 20, 28000000.0000)
INSERT [dbo].[Products] ([ProductID], [ProductName], [CategoryID], [UnitsInStock], [UnitPrice]) VALUES (5, N'MacBook Air M3', 4, 10, 32000000.0000)
INSERT [dbo].[Products] ([ProductID], [ProductName], [CategoryID], [UnitsInStock], [UnitPrice]) VALUES (6, N'Dell XPS 13', 4, 8, 27000000.0000)
INSERT [dbo].[Products] ([ProductID], [ProductName], [CategoryID], [UnitsInStock], [UnitPrice]) VALUES (7, N'Chuot Logitech MX', 5, 50, 900000.0000)
INSERT [dbo].[Products] ([ProductID], [ProductName], [CategoryID], [UnitsInStock], [UnitPrice]) VALUES (8, N'Tai nghe Sony WH-1000XM5', 5, 25, 7500000.0000)
INSERT [dbo].[Products] ([ProductID], [ProductName], [CategoryID], [UnitsInStock], [UnitPrice]) VALUES (9, N'Noi chiên không dau Philips', 6, 12, 3500000.0000)
INSERT [dbo].[Products] ([ProductID], [ProductName], [CategoryID], [UnitsInStock], [UnitPrice]) VALUES (10, N'May hut bui Dyson V15', 6, 6, 13500000.0000)
SET IDENTITY_INSERT [dbo].[Products] OFF
GO
ALTER TABLE [dbo].[Products]  WITH CHECK ADD  CONSTRAINT [FK_Products_Categories] FOREIGN KEY([CategoryID])
REFERENCES [dbo].[Categories] ([CategoryID])
GO
ALTER TABLE [dbo].[Products] CHECK CONSTRAINT [FK_Products_Categories]
GO
USE [master]
GO
ALTER DATABASE [Q2_hienpmhe180216] SET  READ_WRITE 
GO
