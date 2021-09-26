#include "pch.h"
#include "BuiltInFunc.h"
#include <limits.h>

/* ビルド時に C4273 が出るけど、動作してるので気にしない。
 * 気になるならプロジェクト設定で抑制すれば良いと思う。
 */

// 値渡し+値戻し
int sum_int(int x, int y)
{
	return x + y;
}

// 参照渡し
void get_int_max(int *x)
{
	*x = INT_MAX;
}

// 文字列設定
void get_string(char* str, int length)
{
	strcpy_s(str, length, "Hello World! (set from C++Lib)");
}

// 構造体の参照渡し
void get_struct(channels* ch)
{
	ch->b = 0x00;
	ch->g = 0x80;
	ch->r = 0xff;
}
