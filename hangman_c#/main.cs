// Impossible C# Hangman
// CS30 - 14/11/22
// Colby Campbell

using System;
using System.Collections.Generic;

class Program {
  public static void Main (string[] args) {
    // Generate random variable rnd
    Random rnd = new Random();
    
    // Every state of the hangman drawing
    string[] states = {
      "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
      "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
      "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
      "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
      "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
      "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
      "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========="
      };

    // Max number of lives for the user
    int max_lives = states.Length - 1;
    
    // Lives that they are at currently
    int lives = 0;

    // The following two variables are lists instead of arrays as arrays work similarly to tuples in Python
    // Letters that have been guessed wrong
    List<string> wrong_letters = new List<string>();

    // Letters that have been guessed right
    List<string> correct_letters = new List<string>();

    // Words that will be used
    string[] words = {
      "abruptly",
      "absurd",
      "abyss",
      "affix",
      "askew",
      "avenue",
      "awkward",
      "axiom",
      "azure",
      "bagpipes",
      "bandwagon",
      "banjo",
      "bayou",
      "beekeeper",
      "bikini",
      "blitz",
      "blizzard",
      "boggle",
      "bookworm",
      "boxcar",
      "boxful",
      "buckaroo",
      "buffalo",
      "buffoon",
      "buxom",
      "buzzard",
      "buzzing",
      "buzzwords",
      "caliph",
      "cobweb",
      "cockiness",
      "croquet",
      "crypt",
      "curacao",
      "cycle",
      "daiquiri",
      "dirndl",
      "disavow",
      "dizzying",
      "duplex",
      "dwarf",
      "embezzle",
      "equip",
      "espionage",
      "ebola",
      "exodus",
      "faking",
      "fishhook",
      "fixable",
      "fjord",
      "flapjack",
      "flopping",
      "fluffiness",
      "flyby",
      "foxglove",
      "frazzled",
      "frizzled",
      "fuchsia",
      "funny",
      "gabby",
      "galaxy",
      "galvanize",
      "gazebo",
      "gizmo",
      "glowworm",
      "glyph",
      "gnarly",
      "gnostic",
      "gossip",
      "grogginess",
      "haphazard",
      "hyphen",
      "iatrogenic",
      "icebox",
      "injury",
      "ivory",
      "ivy",
      "jackpot",
      "jaundice",
      "jawbreaker",
      "jaywalk",
      "jazziest",
      "jazzy",
      "jelly",
      "jigsaw",
      "jinx",
      "jujitsu",
      "jockey",
      "jogging",
      "joking",
      "jovial",
      "joyful",
      "juicy",
      "jukebox",
      "jumbo",
      "kayak",
      "kazoo",
      "keyhole",
      "khaki",
      "kilobyte",
      "kiosk",
      "kitsch",
      "kiwifruit",
      "klutz",
      "knapsack",
      "larynx",
      "lengths",
      "lucky",
      "luxury",
      "lymph",
      "marquis",
      "matrix",
      "megahertz",
      "microwave",
      "mnemonic",
      "mystify",
      "nowadays",
      "ovary",
      "oxidize",
      "oxygen",
      "pajama",
      "peekaboo",
      "phlegm",
      "pixel",
      "pizazz",
      "pneumonia",
      "polka",
      "pshaw",
      "psyche",
      "puppy",
      "puzzling",
      "quartz",
      "queue",
      "quips",
      "quixotic",
      "quiz",
      "quizzes",
      "quorum",
      "razzmatazz",
      "rhubarb",
      "rhythm",
      "rickshaw",
      "schnapps",
      "scratch",
      "shiv",
      "snazzy",
      "sphinx",
      "spritz",
      "squawk",
      "staff",
      "strength",
      "strengths",
      "stretch",
      "stronghold",
      "stymied",
      "subway",
      "swivel",
      "syndrome",
      "thriftless",
      "thumbscrew",
      "topaz",
      "transcript",
      "transgress",
      "transplant",
      "triathlon",
      "twelfth",
      "twelfths",
      "unknown",
      "unworthy",
      "unzip",
      "uptown",
      "vaporize",
      "vixen",
      "vodka",
      "voodoo",
      "vortex",
      "voyeurism",
      "walkway",
      "waltz",
      "wave",
      "wavy",
      "waxy",
      "wellspring",
      "wheezy",
      "whiskey",
      "whizzing",
      "whomever",
      "wimpy",
      "witchcraft",
      "wizard",
      "woozy",
      "wristwatch",
      "wyvern",
      "xylophone",
      "yachtsman",
      "yippee",
      "yoked",
      "youthful",
      "yummy",
      "zephyr",
      "zigzag",
      "zigzagging",
      "zilch",
      "zipper",
      "zodiac",
      "zombie"
    };

    // Choose a word
    string word = words[rnd.Next(0, words.Length)];

    // Did they win? variable
    bool win;
    
    // While Loop that stops when lives are gone or word guessed
    while (true) {

      // Test for lose; ran out of lives
      if (lives == max_lives) {
        win = false;
        break;
      }

      // Find out what letters the players have gotten so far, and test to see if they won.
      string current_word = null;
      bool underscore_used = false;

      // Loop through every letter in the word
      foreach (char x in word) {
        // Convert char to string
        string letter = x.ToString();

        // This is a boolean so we know if any letters of the current word matched correct_letters
        bool letter_match = false;
        // Loop through every letter in correct_letters
        foreach (string letter2 in correct_letters) {
          // If they are the same letter, append letter to current_word string
          if (letter == letter2) {
            current_word += " " + letter.ToUpper();
            letter_match = true;
          }
        }
          
        // If no letter was found to match, add an underscore and set underscore_used to true
        if (letter_match == false) {
          current_word += " _";
          underscore_used = true;
        }
      }

      // Test for win; got all the letters in the word
      if (underscore_used == false) {
        win = true;
        break;
      }
      
      // Clear screen
      Console.Clear();
      
      // Show the right picture of hangman based on number of lives left
      Console.WriteLine(states[lives]);
      
      // Wrong Letters Shown
      Console.WriteLine("Wrong Guesses: {0}", String.Join(", ", wrong_letters));
      
      // Print letters gotten so far
      Console.WriteLine("{0}:{1}", word.Length, current_word);

      // Ask for guess for letter
      Console.Write("Pick a letter: ");
      
      // Loop until an acceptable answer is given!
      while (true) {
        // Get key input from user and convert to a character and a lowercase string
        Char key = Console.ReadKey(true).KeyChar;
        String guess = key.ToString().ToLower();
  
        // If the letter is in the word, and the letter isn't already in the correct_letters list
        if (word.Contains(guess) && !correct_letters.Contains(guess)) {
          // Append what key they pressed to the correct_letters list (AS A STRING!)
          correct_letters.Add(guess);
          break;
        }
  
        // If the letter is not in the word, and the letter isn't already in the wrong_letters or correct_letters list
        else if (!wrong_letters.Contains(guess) && !correct_letters.Contains(guess) && Char.IsLetter(key)) {
          // Append what key they pressed to the wrong_letters list (AS A STRING!)
          wrong_letters.Add(guess);
          lives += 1;
          break;
        }
      }
    }

    // Clear the screen
    Console.Clear();
    
    // If the player won
    if (win) {
      Console.WriteLine("  +---+\n  |   |\n      |\n \\O/  |\n  |   |\n / \\  |\n=========\nYou win! The word was {0}!", word.ToUpper());
    }

    // If the player lost
    else {
      Console.WriteLine("{0}\nYou lost! The word was {1}!", states[lives], word.ToUpper());
    }
  }
}