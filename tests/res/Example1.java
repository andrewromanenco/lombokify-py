@NoArgsConstructor1
@NoArgsConstructor2(x=2)
public class Example1 {
	int abc() {
		return 123;
	}

	public Example1(int x, double y) {
		super(x);
	}

	public Example1(NotNull.SomeClass obj) {

	}

	public Example1() {
	}

}
