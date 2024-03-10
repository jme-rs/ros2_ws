import { useEffect, useState } from "react";
import { invoke } from "@tauri-apps/api/tauri";

import {
  Dropdown,
  Option,
  Button,
  Field,
} from "@fluentui/react-components";
import styles from "./App.module.scss";
import { goalPoints, Point } from "./goalPoints.d";


export default function App() {

  const [goalPoint, setGoalPoint] = useState<string>("start");

  async function publishKeyInput() {
    console.log("publishKeyInput:", goalPoint);
    await invoke("publish_key_input", { message: goalPoint });
  }

  useEffect(() => {
    console.log("setGoalPoint:", goalPoint);
  }, [goalPoint])


  return (
    <div className={styles.container}>
      <Field label="Select goal point" >
        <div className={styles.field}>
          <Dropdown
            defaultValue={goalPoint}
            selectedOptions={[goalPoint]}
          >
            {
              Array.from(goalPoints.keys()).map((pointName) => (
                <Option
                  key={pointName}

                  value={pointName}
                  onClick={() => {
                    setGoalPoint(pointName);
                  }}
                >
                  {pointName}
                </Option>
              ))
            }
          </Dropdown>

          <Button
            appearance="primary"
            onClick={() => {
              publishKeyInput();
            }}
          >Nav2</Button>
        </div>
      </Field>
    </div>
  );
}
