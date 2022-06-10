# Markdown 
- - -
### 작성방법 셈플들을 작성
- - -
- - -
## 1. Header
샵(#) + 스페이스 + 문자 
```
# H1
## H2
### H3
#### H4
##### H5
###### H6 
```
- - -
- - - 

## 2. 인용문(BlockQuote)
 (>) + 문자
```
> sample 
>> sample 
>>> sample 
```
- - -
- - -
## 3. 글머리 기호: *, +, -
```
- sample 
    + sample 
        * sample 
```
- - - 
- - -
## 4. 코드 블럭
- sample 
(아래 &#96;&#96;&#96; 는 작성이 불가능하여 스페이스 입력함 실제 입력시에는 &#96;&#96;&#96; 로 붙여서 작성)
- 블록 지정후 &#96;&#96;&#96; 입력시 쉽게사용가능
<pre><code>&lt;pre&gt;&lt;code&gt;
public class Sample {
  public static void main(String[] args) {
    System.out.println("Hello!");
  }
}
&lt;/code&gt;&lt;/pre&gt;
</code></pre>
 
```
` ` `
public class Sample {
  public static void main(String[] args) {
    System.out.println("Hello!");
  }
}
` ` `
```

```java
` ` ` 
public class Sample {
  public static void main(String[] args) {
    System.out.println("Hello!");
  }
}
` ` `
```

## 5. 마크다운 특수문자 사용

```
| Symbol | HTML Number | HTML Name | Description              |
|--------|-------------|-----------|--------------------------|
| !      | &#33;       |           | exclamation point        |
| "      | &#34;       | &quot\;   | double quotes            |
| #      | &#35;       |           | number sign              |
| $      | &#36;       |           | dollar sign              |
| %      | &#37;       |           | percent sign             |
| &      | &#38;       | &amp\;    | ampersand                |
| '      | &#39;       |           | single quote             |
| (      | &#40;       |           | opening parenthesis      |
| )      | &#41;       |           | closing parenthesis      |
| *      | &#42;       |           | asterisk                 |
| +      | &#43;       |           | plus sign                |
| ,      | &#44;       |           | comma                    |
| -      | &#45;       |           | minus sign - hyphen      |
| .      | &#46;       |           | period                   |
| /      | &#47;       |           | slash                    |
| :      | &#58;       |           | colon                    |
| ;      | &#59;       |           | semicolon                |
| <      | &#60;       | &lt;      | less than sign           |
| =      | &#61;       |           | equal sign               |
| >      | &#62;       | &gt;      | greater than sign        |
| ?      | &#63;       |           | question mark            |
| @      | &#64;       |           | at symbol                |
| [      | &#91;       |           | opening bracket          |
| \      | &#92;       |           | back slash               |
| ]      | &#93;       |           | closing bracket          |
| ^      | &#94;       |           | caret - circumflex       |
| _      | &#95;       |           | underscore               |
| `      | &#96;       |           | grave accent             |
| {      | &#123;      |           | opening brace            |
| |      | &#124;      |           | vertical bar - pipe      |
| }      | &#125;      |           | closing brace            |
| ~      | &#126;      |           | equivalency sign - tilde |
| –      | &#8211;     |           | en dash                  |
```

## 6. 수평선

- 수평선 
```
***
* * *
---
- - -
```

- sample 

***
* * *
---
- - -

## 7. 글꼴 

```
*single asterisks* -  이탈릭(기울임)

_single underscores_ -  이탈릭(기울임)

**double asterisks** - 굵게

__double underscores__ - 굵게

~~cancelline~~ - 취소선

<U>밑줄</U> - 밑줄

<span style="color:red">RED</span> 

<span style="color:blue">BLUE</span>
```

- Sample 

*single asterisks* -  이탈릭(기울임)

_single underscores_ -  이탈릭(기울임)

**double asterisks** - 굵게

__double underscores__ - 굵게

~~cancelline~~ - 취소선

<U>밑줄</U> - 밑줄

<span style="color:red">RED</span> 

<span style="color:blue">BLUE</span>

## 8. 표
```
- 표는 <span style="color:red">|</span>를 사용하며 두 번째 줄에 있는 <span style="color:red">:</span>의 위치에 따라 해당 열의 정렬을 설정

|a|b|c|d|
|-|-|-|-|
|1|2|3|4|
|5|6|7|8|
```
- Sample 

|a|b|c|d|
|-|-|-|-|
|1|2|3|4|
|5|6|7|8|

## 9. 링크
```
[네이버](https://www.naver.com)로 << 네이버 클릭! 
```
- Sample 

[네이버](https://www.naver.com) << 네이버 클릭!

## 10. 이미지
```
이미지 주소를활용
```
```
![Alt text](/path/img.jpg)
![Alt text](/path/img.jpg "Optional title")
<img width="" height=""></img>
```
![git](https://images.velog.io/images/gparkkii/post/7939a185-383b-4191-9fc6-22051ddf5094/github-white-logo-700-740x395.png "git cat")
