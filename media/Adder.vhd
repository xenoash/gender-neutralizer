
------------------------------------------------------ 
--  Library Name :  work 
--  Unit    Name :  carry_select_adder32 
--  Description : structural design of 32-bit carry select adder 
------------------------------------------------------ 

library IEEE;
use IEEE.std_logic_1164.all;

entity Adder is
  --generic (N : natural := 1);              -- Range parameter
  port 
  (A :in std_logic_vector(31 downto 0);
   S :out std_logic_vector(32 downto 0) := "000000000000000000000000000000000";
   CLK, CLR, LOAD:in std_logic;
   END_FLAG:out std_logic:='0');
  end Adder;
  
  architecture adder_stru of adder is
  
  component reg32 is
    --generic (N : natural := 1);
    port
    (data_in: in std_logic_vector(31 downto 0);
     load, reset: in std_logic;
     data_out: out std_logic_vector(31 downto 0));
   end component;

  component carry_select_adder32 is
    --generic (N : natural := 1);
    port 
    (A, B :in std_logic_vector(31 downto 0);
     cin: in std_logic;
     S:out std_logic_vector(31 downto 0);
     cout:out std_logic);
  end component;
  
  component reg33 is
    --generic (N : natural := 1);
    port
    (data_in: in std_logic_vector(32 downto 0);
    load, reset: in std_logic;
    data_out: out std_logic_vector(32 downto 0));
  end component;
    
    signal tempA : STD_LOGIC_VECTOR(31 DOWNTO 0) := "00000000000000000000000000000000";
    signal tempS1, tempS2 : STD_LOGIC_VECTOR(32 DOWNTO 0) := "000000000000000000000000000000000";
    
    begin
      
      regA: reg32                port map(A(31 downto 0),       LOAD,                CLR,    tempA(31 downto 0));
      CSLA: carry_select_adder32 port map(tempA(31 downto 0),   tempS2(31 downto 0), tempS2(32),  tempS1(31 downto 0), tempS1(32));
      regZ: reg33                port map(tempS1(32 downto 0),  LOAD,                CLR,    tempS2(32 downto 0));
      S(32 downto 0) <= tempS2(32 downto 0);
        
    end adder_stru;