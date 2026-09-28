class SignalController:
    name = "Adaptive & Emergency Logic"

    @staticmethod
    def compute_signal_state(lane_1_count: int, lane_2_count: int, emergency: bool):
        """
        Calculates active green signal and timer duration.
        If emergency is True, forces priority green override.
        """
        if emergency:
            # Grant priority to the lane with emergency or default to lane 1
            return {"active_signal": 1, "duration": 30, "override": True}

        # Dynamic density proportional timing
        if lane_1_count >= lane_2_count:
            return {"active_signal": 1, "duration": max(10, lane_1_count * 2), "override": False}
        else:
            return {"active_signal": 2, "duration": max(10, lane_2_count * 2), "override": False}