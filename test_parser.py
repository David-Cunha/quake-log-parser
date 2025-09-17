# test_parser.py
import unittest
import os
# Importa a função que queremos testar do nosso outro arquivo
from parser import parse_quake_log

class TestQuakeLogParser(unittest.TestCase):

    def setUp(self):
        # Cria um arquivo de log falso para cada teste
        self.test_log_file = 'test_log.log'
        mock_log_content = """
          0:00 InitGame: ...
         21:22 Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT
         21:42 Kill: 3 2 10: Zeh killed Isgalamido by MOD_RAILGUN
         22:04 ShutdownGame:
         23:00 InitGame: ...
         23:20 Kill: 1022 2 22: <world> killed Mocinha by MOD_FALLING
         24:00 ShutdownGame:
        """
        with open(self.test_log_file, "w") as f:
            f.write(mock_log_content)

        self.parsed_data = parse_quake_log(self.test_log_file)

    def tearDown(self):
        # Remove o arquivo de log falso após cada teste
        os.remove(self.test_log_file)

    def test_game_count(self):
        self.assertEqual(len(self.parsed_data), 2, "Deveria encontrar 2 partidas")

    def test_game_1_data(self):
        game_1 = self.parsed_data.get('game_1')
        self.assertIsNotNone(game_1)
        self.assertEqual(game_1['total_kills'], 2)
        self.assertListEqual(game_1['players'], ['Isgalamido', 'Zeh'])
        self.assertEqual(game_1['kills'].get('Isgalamido', 0), -1)
        self.assertEqual(game_1['kills'].get('Zeh', 0), 1)

    def test_kills_by_means(self):
        game_1 = self.parsed_data.get('game_1')
        self.assertEqual(game_1['kills_by_means']['MOD_TRIGGER_HURT'], 1)
        self.assertEqual(game_1['kills_by_means']['MOD_RAILGUN'], 1)

if __name__ == '__main__':
    unittest.main()