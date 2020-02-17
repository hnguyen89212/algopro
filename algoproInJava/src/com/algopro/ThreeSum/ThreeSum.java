package com.algopro.ThreeSum;

import java.util.ArrayList;
import java.util.Arrays;

public class ThreeSum {

	public static int[][] Solution(int[] nums) {
		ArrayList<Integer[]> list = new ArrayList<>();
		Arrays.sort(nums);
		//
		for (int i = 0; i < nums.length - 2; i++) {
			if (i > 0 && nums[i] == nums[i - 1])
				continue;
			// two sum
			int j = i + 1;
			int k = nums.length - 1;
			while (j < k) {
				int sum = nums[i] + nums[j] + nums[k];
				if (sum == 0) {
					list.add(new Integer[] { nums[i], nums[j], nums[k] });
					while (j < k && nums[j] == nums[j + 1])
						j++;
					while (j < k && nums[k] == nums[k - 1])
						k--;
					j++;
					k--;
				} else if (sum > 0) {
					k--;
				} else {
					j++;
				}
			}
			// end of two sum
		}
		//
		int[][] res = new int[list.size()][3];
		for (int i = 0; i < list.size(); i++) {
			Integer[] tmp = list.get(i);
			res[i] = new int[] { tmp[0], tmp[1], tmp[2] };
		}
		return res;
	}

	public static void main(String[] args) {
		int[] test = { -1, 0, 1, 2, -1, -4 };
		int[][] solutions = Solution(test);
		for (int i = 0; i < solutions.length; i++) {
			for (int j = 0; j < solutions[i].length; j++) {
				System.out.print(solutions[i][j] + " ");
			}
			System.out.println();
		}
	}

}
