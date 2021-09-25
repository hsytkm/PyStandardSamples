#include "pch.h"
#include "BuiltInFunc.h"

/* ビルド時に C4273 が出るけど、動作してるので気にしない。
 * 気になるならプロジェクト設定で抑制すれば良いと思う。
 */

int sum_int(int x, int y)
{
	return x + y;
}

