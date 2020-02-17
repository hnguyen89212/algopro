package com.algopro.RansomNote;

import java.util.HashMap;

public class RansomNote {

	/**
	 * <h1>ALGORITHM:</h1>
	 * <ul>
	 * <li>Construct a map (key is unique) of key, value pairs where:
	 * <ol>
	 * <li>key = character appearing in magazine</li>
	 * <li>value = appearances of the respective key</li>
	 * </ol>
	 * </li>
	 * <li>Iterate through the ransomeNote string:
	 * <ol>
	 * <li>Extract a current character</li>
	 * <li>If the map does not contain such character, return false.</li>
	 * <li>Else decrement the value (appearances) of the character in the map by
	 * one.</li>
	 * <li>If after decrement, the character's appearance is less than 0, return
	 * false.</li>
	 * </ol>
	 * </li>
	 * <li>At the exit point, return true.</li>
	 * </ul>
	 * 
	 * @param ransomNote
	 * @param magazine
	 * @return true if ransomNote can be constructed from magazine; false otherwise.
	 */
	public static boolean Solution(String ransomNote, String magazine) {
		HashMap<Character, Integer> mag_dict = new HashMap<>();
		// Construct the map
		for (int i = 0; i < magazine.length(); i++) {
			char ch = magazine.charAt(i);
			if (mag_dict.containsKey(ch))
				mag_dict.put(ch, mag_dict.get(ch) + 1);
			else
				mag_dict.put(ch, 1);
		}
		// Iterate through the ransom note
		for (int i = 0; i < ransomNote.length(); i++) {
			char ch = ransomNote.charAt(i);
			// If the map does not contain such character, return false
			if (!mag_dict.containsKey(ch))
				return false;
			// Decrement appearance
			int appearance = mag_dict.get(ch) - 1;
			if (appearance < 0)
				return false;
			// If appearance > 0, update it
			mag_dict.put(ch, appearance);
		}
		// At this point, reconstruction should be viable.
		return true;
	}

	public static void main(String[] args) {
		System.out.println(Solution("aa", "abc"));
		System.out.println(Solution("abv", "aabc"));
	}

}
