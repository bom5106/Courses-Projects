
using System;

namespace myFirstConsole
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            Console.WriteLine("Give me your name ");
            var name = Console.ReadLine();

            Console.WriteLine("Hello, " + name);
            //or
            Console.WriteLine($"{Environment.NewLine}Hello, {name}");
        }
    }
}