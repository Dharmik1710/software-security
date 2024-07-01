use std::env;
use std::fs::File;
use std::io::{self, Write};


fn add(n1: u32, n2: u32) -> u32 {
    let res: u32 = n1 + n2;
    return res;
}

fn sub(n1: u32, n2: u32) -> u32 {
    let res: u32 = n1 - n2;
    return res;
}

fn mul(n1: u32, n2: u32) -> u32 {
    let res: u32 = n1 * n2;
    return res;
}

fn int_div(n1: u32, n2: u32) -> u32 {
    let res: u32 = n1 / n2;
    return res;
}

fn real_div(n1: u32, n2: u32) -> f32 {
    let res: f32 = n1 as f32 / n2 as f32;
    return res;
}

fn main() {

    // file arguments 
    // partial code for writing to file taken from chatgpt
    let args: Vec<String> = env::args().collect();
    let mut output_file: Option<File> = None;
    if args.len() > 1 {
        let filename = &args[1];
        match File::create(filename) {
            Ok(file) => output_file = Some(file),
            Err(err) => eprintln!("Failed to create file: {}", err),
        }
    }


    // Create mutable string
    let mut raw_inp_op = String::new();
    let mut raw_inp_num_1 = String::new();
    let mut raw_inp_num_2 = String::new();
    let mut output_str: String = String::new();
    let mut prev_result: Option<String> = None;


    let add_op = "+";
    let sub_op = "-";
    let mul_op = "*";
    let int_div_op = "//";
    let real_div_op = "/";
    let exit = "exit";
    
    loop {

        print!("Input operation: ");
        io::stdout().flush().unwrap();
        // Read input from stdin
        io::stdin().read_line(&mut raw_inp_op).expect("Failed to read line");
        // Trim whitespace from input
        let op = raw_inp_op.trim();

        // if user inputs exit, then save and exit
        if op == exit {
            // Save last result to file if specified
            if let Some(file) = &mut output_file {
                if let Some(result) = &prev_result {
                    if let Err(err) = writeln!(file, "{}", result) {
                        eprintln!("Failed to write to file: {}", err);
                    }
                }
            }
            break;
        }


        print!("Number 1: ");
        io::stdout().flush().unwrap();
        // integer 1
        io::stdin().read_line(&mut raw_inp_num_1).expect("Failed to read line");
        let n1: u32 = raw_inp_num_1.trim().parse().unwrap();

        print!("Number 2: ");
        io::stdout().flush().unwrap();
        // integer 2
        io::stdin().read_line(&mut raw_inp_num_2).expect("Failed to read line");
        let n2: u32 = raw_inp_num_2.trim().parse().unwrap();
        
        // Check user input
        if op == add_op {
            let res = add(n1, n2);
            prev_result = Some(format!("{}", res));
            output_str = format!("Requested operation was {} ({}) and the result is: {}", "addition", "+", res);
        } else if op == sub_op {
            let res = sub(n1, n2);
            prev_result = Some(format!("{}", res));
            output_str = format!("Requested operation was {} ({}) and the result is: {}", "subtraction", "-", res);
        } else if op == mul_op {
            let res = mul(n1, n2);
            prev_result = Some(format!("{}", res));
            output_str = format!("Requested operation was {} ({}) and the result is: {}", "addition", "+", res);
        } else if op == int_div_op {
            let res = int_div(n1, n2);
            prev_result = Some(format!("{}", res));
            output_str = format!("Requested operation was {} ({}) and the result is: {}", "addition", "+", res);
        } else if op == real_div_op {
            let res = real_div(n1, n2);
            prev_result = Some(format!("{}", res));
            output_str = format!("Requested operation was {} ({}) and the result is: {}", "addition", "+", res);
        } else {
            println!("Invalid input");
            continue;
        }

        println!("{}", output_str);
        
        // Clear op string for next iteration
        raw_inp_op.clear();
        raw_inp_num_1.clear();
        raw_inp_num_2.clear();
        output_str.clear();
    }
}
