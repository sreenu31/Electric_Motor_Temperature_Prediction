import pathlib

import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score


def main() -> None:
    root_dir = pathlib.Path(__file__).resolve().parent
    data_path = root_dir / "pmsm_temperature_data.csv"
    output_dir = root_dir / "Flask"

    df = pd.read_csv(data_path)
    df = df.drop(
        ["profile_id", "torque", "stator_yoke", "stator_tooth", "stator_winding"],
        axis=1,
    )

    x = df.drop("pm", axis=1)
    y = df["pm"]

    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)

    x_train, x_test, y_train, y_test = train_test_split(
        x_scaled, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)
    print(f"R2 Score: {r2_score(y_test, y_pred):.6f}")
    print(f"MSE: {mean_squared_error(y_test, y_pred):.6f}")

    output_dir.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, output_dir / "model.save")
    joblib.dump(scaler, output_dir / "transform.save")


if __name__ == "__main__":
    main()
